class ReferenceBooks:

    def __init__(self, url):
        self.url = f'{url}/v1/reference-books'

    def court_decision_types(self, ses):
        response = ses.request(method='get', url=f'{self.url}/court-decision-types', verify=False)
        result = response.json() if response.status_code == 200 else response
        return result

    def message_types(self, ses):
        response = ses.request(method='get', url=f'{self.url}/message-types', verify=False)
        result = response.json() if response.status_code == 200 else response
        return result
