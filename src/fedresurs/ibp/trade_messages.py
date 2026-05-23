from .api import BaseAPI


class TradeMessagesAPI(BaseAPI):

    def __init__(self, url):
        super().__init__(url)
        self.url = f'{url}/v1/trade-messages'

    def execute(self, ses, **kwargs):
        self._prepare_params(**kwargs)
        response = ses.request(method='get', url=self.url, params=self.params, verify=False)
        result = response.json() if response.status_code == 200 else response
        return result

    def by_id(self, ses, guid):
        response = ses.request(method='get', url=f'{self.url}/{guid}', verify=False)
        result = response.json() if response.status_code == 200 else response
        return result

    def files(self, ses, guid):
        response = ses.request(method='get', url=f'{self.url}/{guid}/files/archive', verify=False)
        result = response.content if response.status_code == 200 else response
        return result


class TradeMessages:

    def __init__(self, **kwargs):
        self.guid = kwargs.get('guid')
        self.number = None
        self.date_publish = None
        self.date_event = None
        self.is_current = None
        self.type = None
        self.is_locked = None
        self.content = None
        self.trade_place_guid = None
        self.bankrupt_guid = None
        self.auction_message_guid = None
        self.trade = None

    def info(self, json):
        self.guid = json['guid'] | None
        self.number = json['number'] | None
        self.date_publish = json['datePublish'] | None
        self.date_event = json['dateEvent'] | None
        self.is_current = json['isCurrent'] | None
        self.type = json['type'] | None
        self.is_locked = json['isLocked'] | None
        self.content = json['content'] | None
        self.trade_place_guid = json['tradePlaceGuid'] | None
        self.bankrupt_guid = json['bankruptGuid'] | None
        self.auction_message_guid = json['auctionMessageGuid'] | None
        self.trade = json['trade'] | None




