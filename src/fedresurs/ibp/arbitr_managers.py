from .api import BaseAPI


class ArbitrManagersAPI(BaseAPI):

    def __init__(self, url):
        super().__init__(url)
        self.url = f'{url}/v1/arbitr-managers'

    def execute(self, ses, **kwargs):
        self._prepare_params(**kwargs)
        response = ses.request(method='get', url=self.url, params=self.params, verify=False)
        result = response.json() if response.status_code == 200 else response
        return result
