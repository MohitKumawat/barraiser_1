from api.MockServices.mock import Mock

mock_serice = Mock()
def notify(number, message, type='MSG'):
    try:
        if type == 'MSG':
            data = {
                "phone_number": number,
                "message": message
            }
            res = mock_serice.send(data)
            return res
    except:
        return None