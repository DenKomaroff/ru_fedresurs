import json


class Auth:

    def __init__(self, url, login, pwd):
        self.url = f'{url}/v1/auth'
        self.login = login
        self.pwd = pwd
        self.token = None

    def execute(self, ses):
        payload = {
            'login': self.login,
            'password': self.pwd
        }
        payload = json.dumps(payload).encode('utf-8')
        response = ses.request(method='post', url=self.url, data=payload, verify=False)
        self.token = response.json()['jwt'] if response.status_code == 200 else None
        return self
