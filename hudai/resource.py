from hudai import HudAiError
from hudai.client import HudAi

class Resource(object):
    def __init__(self, client):
        """
        :param client: API client
        """

        if client is None or type(client) is not HudAi:
            raise HudAiError('client required', 'initialization_error')

        self._client = client
        self._base_path = '/'

    def _request(self, request_params):
        """
        Abstracted request method, request config is defined in the resource itself
        :param params:
        :return:
        """
        method = request_params.get('method', 'GET')
        params = request_params.get('params', {})
        path = self._build_path(request_params)
        data = request_params.get('data', {})

        return self._client.make_request(method, path, params, data)

    def _build_path(self, params):
        """
        Build the url path string
        :return url:
        """
        path = self._base_path + params.get('url', '')
        params = params.get('params')

        if params is None:
            return path

        return path.format(**params)
