from os import getenv
from pydash import map_keys
from requests import Request, Session
from hudai.error import HudAiError

class Resource(object):
    def __init__(self, secret_key):
        """
        :param secret_key: API secret key
        """
        self.secret_key = secret_key

        if self.secret_key is None:
            raise HudAiError('Missing required "secretKey".', 'authentication_error')

    def make_request(self, request_config):
        """
        Abstracted request method, request config is defined in the resource itself
        :param request_config:
        :return:
        """
        base_url = getenv('HUDAI_API_BASE_URL', 'https://api.hud.ai/v1')
        session = Session()
        req = Request(
            request_config.method,
            base_url + self.build_url(request_config),
            data=request_config.data,
            params=request_config.query
        )
        prepared = req.prepare()
        prepared.headers['User-Agent'] = 'Hud.ai python v1.0.0 +(https://github.com/FoundryAI/hud-ai-python#readme)'
        prepared.headers['x-api-key'] = self.secret_key
        return session.send(prepared).json()

    def build_url(request_config):
        """
        Build the url path string
        :return url:
        """
        url = request_config.url
        map_keys(request_config.params, lambda value, key: url.replace('{' + key + '}', value))
        return url
