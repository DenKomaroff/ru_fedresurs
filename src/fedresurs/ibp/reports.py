from .api import BaseApi


class Reports(BaseApi):

    def __init__(self, url):
        super().__init__(url)
        self.url = f'{url}/v1/reports'

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

    def linked(self, ses, guid):
        response = ses.request(method='get', url=f'{self.url}/{guid}/linked', verify=False)
        result = response.json() if response.status_code == 200 else response
        return result
