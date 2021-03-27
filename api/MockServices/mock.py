import requests

class Mock:
    '''https://run.mocky.io/v3/fd99c100-f88a-4d70-aaf7-393dbbd5d99f
Sample request: {"phone_number": "9999999999", "message": "Too many 5xx!"}'''
    def send(self, data):
        post_data = data

        response = requests.post('https://run.mocky.io/v3/fd99c100-f88a-4d70-aaf7-393dbbd5d99f', data=post_data)
        content = response.content
        return content
