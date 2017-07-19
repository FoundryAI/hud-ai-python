from hudai import HudAiError

class Resource(object):
    def __init__(self, client, base_path=''):
        """
        :param client: API client
        """

        if client is None:
            raise HudAiError('client required', 'initialization_error')

        self._client = client
        self._base_path = base_path


    def request(self, params):
        """
        Abstracted request method, request config is defined in the resource itself
        :param params:
        :return:
        """
        method = params.get('method', 'GET')
        query_params = params.get('params', {})
        url = params.get('url', '')
        payload = params.get('data', {})

        path = self._build_path(url, query_params)

        if method.lower() == 'get':
            return self._client.get(path, params=params)

        if method.lower() == 'post':
            return self._client.post(path, params=params, data=payload)

        if method.lower() == 'put':
            return self._client.put(path, params=params, data=payload)

        if method.lower() == 'patch':
            return self._client.patch(path, params=params, data=payload)

        if method.lower() == 'delete':
            return self._client.delete(path, params=params)

        raise ValueError('method.invalid:{}'.format(method))


    def _build_path(self, url, query_params):
        """
        Build the url path string
        :return url:
        """
        path = "{}{}".format(self._base_path, url)

        if query_params is None:
            return path

        return path.format(**query_params)
