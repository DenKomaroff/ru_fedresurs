from requests import Session
from urllib3 import disable_warnings
from .am_sro_memberships import AmSroMembershipsAPI
from .arbitr_managers import ArbitrManagersAPI
from .auth import AuthAPI
from .bankrupts import BankruptsAPI
from .bankrupts_merged import BankruptsMergedAPI
from .company_trade_orgs import CompanyTradeOrgsAPI
from .messages import MessagesAPI
from .person_trade_orgs import PersonTradeOrgsAPI
from .reference_books import ReferenceBooksAPI
from .reports import ReportsAPI
from .sros import SrosAPI
from .trade_messages import TradeMessagesAPI
from .trade_places import TradePlacesAPI

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
        return AmSroMembershipsAPI(url=self.url).execute(self.session, **kwargs)

    def arbitral_managers(self, **kwargs):
        return ArbitrManagersAPI(url=self.url).execute(self.session, **kwargs)

    def auth(self):
        return AuthAPI(url=self.url, login=self.login, pwd=self.pwd).execute(self.session)

    def bankrupts(self, **kwargs):
        return BankruptsAPI(url=self.url).execute(self.session, **kwargs)

    def bankrupts_merged(self, **kwargs):
        return BankruptsMergedAPI(url=self.url).execute(self.session, **kwargs)

    def company_trade_orgs(self, **kwargs):
        return CompanyTradeOrgsAPI(url=self.url).execute(self.session, **kwargs)

    def messages(self, **kwargs):
        return MessagesAPI(url=self.url).execute(self.session, **kwargs)

    def message(self, guid):
        return MessagesAPI(url=self.url).by_id(self.session, guid)

    def message_files(self, guid):
        return MessagesAPI(url=self.url).files(self.session, guid)

    def message_linked(self, guid):
        return MessagesAPI(url=self.url).linked(self.session, guid)

    def person_company_trade_orgs(self, **kwargs):
        return PersonTradeOrgsAPI(url=self.url).execute(self.session, **kwargs)

    def court_decision_types(self):
        return ReferenceBooksAPI(url=self.url).court_decision_types(self.session)

    def message_types(self):
        return ReferenceBooksAPI(url=self.url).message_types(self.session)

    def reports(self, **kwargs):
        return ReportsAPI(url=self.url).execute(self.session, **kwargs)

    def report(self, guid):
        return ReportsAPI(url=self.url).by_id(self.session, guid)

    def report_files(self, guid):
        return ReportsAPI(url=self.url).files(self.session, guid)

    def report_linked(self, guid):
        return ReportsAPI(url=self.url).linked(self.session, guid)

    def sros(self, **kwargs):
        return SrosAPI(url=self.url).execute(self.session, **kwargs)

    def trade_messages(self, **kwargs):
        return TradeMessagesAPI(url=self.url).execute(self.session, **kwargs)

    def trade_message(self, guid):
        return TradeMessagesAPI(url=self.url).by_id(self.session, guid)

    def trade_message_files(self, guid):
        return TradeMessagesAPI(url=self.url).files(self.session, guid)

    def trade_places(self, **kwargs):
        return TradePlacesAPI(url=self.url).execute(self.session, **kwargs)

