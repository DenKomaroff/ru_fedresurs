class BaseApi:

    def __init__(self, url):
        pass

    def _prepare_params(self, **kwargs):
        params = None
        if len(kwargs) > 0:
            params = {}
            for param in kwargs:
                params.update({param.replace('_', '.'): kwargs.get(param)})
        self.params = params
