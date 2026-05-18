from requests import Session
from urllib3 import disable_warnings
from .auth import Auth
from .messages import Messages
from .message_docs import MessageDocs

PROD_HOST = 'sfact-messages-prod.fedresurs.ru'
DEMO_HOST = 'sfact-messages-demo.fedresurs.ru'
DEMO_LOGIN = 'demo'
DEMO_PWD = 'Ax!761BN'

# 'https://sfact-messages-demo.fedresurs.ru/swagger/index.html'

class InterfaxSpecMessages:

    def __init__(self, login=None, password=None):
        self.host = DEMO_HOST
        self.url = f'https://{self.host}'
        self.login = login or DEMO_LOGIN
        self.pwd = password or DEMO_PWD
        disable_warnings()

    def __enter__(self):
        self.session=Session()
        self.session.headers.update({'Accept': 'application/json, text/plain, */*'})
        self.session.headers.update({'accept-encoding': 'gzip, deflate, br, zstd'})
        self.session.headers.update({'Connection': 'keep-alive'})
        self.session.headers.update({'Content-Type': 'application/json, charset=UTF-8'})
        self.token = self.auth().token
        self.session.headers.update({'Authorization': f'Bearer {self.token}'})
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def auth(self):
        return Auth(url=self.url, login=self.login, pwd=self.pwd).execute(self.session)

    def messages(self, **kwargs):
        return Messages(url=self.url).execute(self.session, **kwargs)

    def message(self, guid):
        return Messages(url=self.url).by_id(self.session, guid)

    def message_docs(self, guid):
        return MessageDocs(url=self.url).by_id(self.session, guid)

