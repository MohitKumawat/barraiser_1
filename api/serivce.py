from api.models import Team, Developers
from django_auth.constants import SUCCESS, FAILURE
from notification.notification_service import notify


def validate_team_data(data):
    return {
        'status': SUCCESS,
        'message': 'Success'
    }


def add_team_data(data):
    team_name = data.get('team', {}).get('name')
    if team_name is None:
        return {
            'status': FAILURE,
            'message': 'Team Name does not exist'
        }
    team_res = Team.add_team(team_name)
    if team_res.get('status', FAILURE) == FAILURE:
        return team_res
    team_id = team_res['data'].id
    developers = data.get('developers', list)
    errors = []
    developer_ids = []

    for developer in developers:
        dev_res = Developers.add_developer(developer, team_id)
        if dev_res.get('status') == SUCCESS:
            developer_ids.append(dev_res['data'].id)
        else:
            errors.append(dev_res.get('message', ''))
    data = {
        'team_id': team_id,
        'developer_ids': developer_ids
    }
    return {
        'status': SUCCESS if not errors else FAILURE,
        'message': ', '.join(errors),
        'data': data
    }

def prepare_notification(team_id, message):
    res = get_member_details(team_id)
    if res:
        res = notify(res, message)
        return {
            'status': FAILURE,
            'message': f'{res}'
        }
    else:
        return {
            'status': FAILURE
        }
def get_member_details(team_id):
    dev = Developers.objects.filter(team_id=team_id).first()
    if dev:
        return dev.phone_number
    return None