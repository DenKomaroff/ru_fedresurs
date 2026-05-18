import json
from hashlib import sha512


class Auth:

    def __init__(self, url, login, pwd):
        self.url = f'{url}/v1/auth'
        self.login = login
        self.pwd = pwd
        self.hash = None
        self.token = None

    def execute(self, ses):
        sha = sha512()
        sha.update(self.pwd.encode('utf-8'))
        self.hash = sha.hexdigest()
        payload = {
            'login': self.login,
            'passwordHash': self.hash
        }
        payload = json.dumps(payload).encode('utf-8')
        response = ses.request(method='post', url=self.url, data=payload, verify=False)
        self.token = response.json()['jwt'] if response.status_code == 200 else None
        return self
