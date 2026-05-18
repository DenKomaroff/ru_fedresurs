class AmSroMemberships:

    def __init__(self, url):
        self.url = f'{url}/v1/am-sro-memberships'

    def execute(self, ses, **kwargs):
        params = None
        if len(kwargs) > 0:
            params = {}
            for param in kwargs:
                params.update({param: kwargs.get(param)})
        response = ses.request(method='get', url=self.url, params=params, verify=False)
        result = response.json() if response.status_code == 200 else response
        return result
