import pytest
from pytest_mock import mocker

from hudai.client import HudAi
from hudai.resource import Resource

client = HudAi(api_key='mock-api-key')

def test_standard_http_verbs_available():
    resource = Resource(client)

    assert callable(resource.get)
    assert callable(resource.post)
    assert callable(resource.put)
    assert callable(resource.patch)
    assert callable(resource.delete)

@pytest.mark.parametrize('http_verb', [('get'),('post'),('put'),('patch'),('delete')])
def test_parameter_injection(mocker, http_verb):
    mocker.patch.object(client, http_verb, autospec=True)
    resource = Resource(client)

    path = '/test/{replace_me}/path'
    params = {'params': {'replace_me': 'replaced'}}

    # Actual function call, e.g. resource.get(path, params)
    getattr(resource, http_verb)(path, params)

    getattr(client, http_verb).assert_called_once_with(
        '/test/replaced/path',
        params={'replace_me': 'replaced'})
