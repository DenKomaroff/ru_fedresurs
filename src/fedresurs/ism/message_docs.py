class MessageDocs:

    def __init__(self, url):
        self.url = f'{url}/v1/messagedocs'

    def by_id(self, ses, guid):
        response = ses.request(method='get', url=f'{self.url}/{guid}', verify=False)
        result = response.json() if response.status_code == 200 else response
        return result
