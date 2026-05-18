from requests import Session
from urllib3 import disable_warnings
from .am_sro_memberships import AmSroMemberships
from .arbitr_managers import ArbitrManagers
from .auth import Auth
from .bankrupts import Bankrupts
from .bankrupts_merged import BankruptsMerged
from .company_trade_orgs import CompanyTradeOrgs
from .messages import Messages
from .person_trade_orgs import PersonTradeOrgs
from .reference_books import ReferenceBooks
from .reports import Reports
from .sros import Sros
from .trade_messages import TradeMessages
from .trade_places import TradePlaces

PROD_HOST = 'bank-publications-prod.fedresurs.ru'
DEMO_HOST = 'bank-publications-demo.fedresurs.ru'
DEMO_LOGIN = 'demowebuser'
DEMO_PWD = 'Ax!761BN'

# 'https://bank-publications-demo.fedresurs.ru/swagger/index.html'

class InterfaxBankruptcyPublications:

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

    def am_sro_memberships(self, **kwargs):
        return AmSroMemberships(url=self.url).execute(self.session, **kwargs)

    def arbitral_managers(self, **kwargs):
        return ArbitrManagers(url=self.url).execute(self.session, **kwargs)

    def auth(self):
        return Auth(url=self.url, login=self.login, pwd=self.pwd).execute(self.session)

    def bankrupts(self, **kwargs):
        return Bankrupts(url=self.url).execute(self.session, **kwargs)

    def bankrupts_merged(self, **kwargs):
        return BankruptsMerged(url=self.url).execute(self.session, **kwargs)

    def company_trade_orgs(self, **kwargs):
        return CompanyTradeOrgs(url=self.url).execute(self.session, **kwargs)

    def messages(self, **kwargs):
        return Messages(url=self.url).execute(self.session, **kwargs)

    def message(self, guid):
        return Messages(url=self.url).by_id(self.session, guid)

    def message_files(self, guid):
        return Messages(url=self.url).files(self.session, guid)

    def message_linked(self, guid):
        return Messages(url=self.url).linked(self.session, guid)

    def person_company_trade_orgs(self, **kwargs):
        return PersonTradeOrgs(url=self.url).execute(self.session, **kwargs)

    def court_decision_types(self):
        return ReferenceBooks(url=self.url).court_decision_types(self.session)

    def message_types(self):
        return ReferenceBooks(url=self.url).message_types(self.session)

    def reports(self, **kwargs):
        return Reports(url=self.url).execute(self.session, **kwargs)

    def report(self, guid):
        return Reports(url=self.url).by_id(self.session, guid)

    def report_files(self, guid):
        return Reports(url=self.url).files(self.session, guid)

    def report_linked(self, guid):
        return Reports(url=self.url).linked(self.session, guid)

    def sros(self, **kwargs):
        return Sros(url=self.url).execute(self.session, **kwargs)

    def trade_messages(self, **kwargs):
        return TradeMessages(url=self.url).execute(self.session, **kwargs)

    def trade_message(self, guid):
        return TradeMessages(url=self.url).by_id(self.session, guid)

    def trade_message_files(self, guid):
        return TradeMessages(url=self.url).files(self.session, guid)

    def trade_places(self, **kwargs):
        return TradePlaces(url=self.url).execute(self.session, **kwargs)

