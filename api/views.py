from django.core.handlers import exception
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serivce import validate_team_data, add_team_data, prepare_notification
from django_auth.constants import FAILURE, SUCCESS


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def hello_world(request):
    print(request.data)
    date = {'hello': 'Hello World'}
    return Response(data=date, status=status.HTTP_200_OK)



def validate_team_data2(fx):
    def inner(*args, **kwargs):
        data = args[0].data
        if not data:
            return  Response(data = {}, status=status.HTTP_400_BAD_REQUEST)
        if 'team' not in data:
            pass
        else:
            pass
        if 'developers' not in data:
            pass
        else:
            if type(data['developers']) is not list:
                return Response(data={'error': 'developr type mismatch'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                for developer in data['developers']:
                    pass
        return fx(*args, **kwargs)
    return inner


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@validate_team_data2
def add_team(request):
    data = request.data
    # validation_res = validate_team_data(data)
    # if validation_res.get('status', FAILURE) == FAILURE:
    #     return Response(data={}, status=status.HTTP_400_BAD_REQUEST)
    res = add_team_data(data)

    return Response(data=res, status=status.HTTP_200_OK if res.get('status') == SUCCESS else status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def notify_team(request):
    data = request.data
    id = data.get('id')
    msg = data.get('message', '')
    res = prepare_notification(id, msg)
    return Response(data=res, status=status.HTTP_200_OK if res.get('status') == SUCCESS else status.HTTP_500_INTERNAL_SERVER_ERROR)
