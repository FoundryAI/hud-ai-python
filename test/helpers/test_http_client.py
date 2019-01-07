"""HUD.ai HTTP Client Specs

Ensure that the client continues to act in a predictable way so that it can be
injected into Resources or used directly to perform the required translations
and inject any required headers
"""

from datetime import datetime
import pytest
import requests

from hudai import Client as HudAi
from hudai.helpers.http_client import HttpClient

hud_client = HudAi(client_id='mock-client-id')
base_url = 'https://api.hud.ai/v1'

@pytest.mark.parametrize('http_verb', [('get'), ('post'), ('put'), ('patch'), ('delete')])
def test_required_parameter_injection(mocker, http_verb):
    http_client = HttpClient(hud_client, base_url)
    mocker.patch.object(requests, http_verb)
    mocker.patch.object(hud_client, 'access_token', 'fake-access-token')

    # Actual function call, e.g. http_client.get(path, params)
    function_under_test = getattr(http_client, "http_{}".format(http_verb))
    requests_function = getattr(requests, http_verb)

    assert callable(function_under_test)

    function_under_test('/test/url')

    assert requests_function.call_count == 1

    args, kwargs = requests_function.call_args

    assert args[0] == 'https://api.hud.ai/v1/test/url'
    assert kwargs['headers']['Authorization'] == 'Bearer fake-access-token'


@pytest.mark.parametrize('http_verb', [('get'), ('delete')])
def test_passing_requests_params(mocker, http_verb):
    http_client = HttpClient(hud_client, base_url)
    mocker.patch.object(requests, http_verb)

    # Actual function call, e.g. http_client.get(path, params)
    function_under_test = getattr(http_client, "http_{}".format(http_verb))
    requests_function = getattr(requests, http_verb)

    function_under_test('/test/url', query_params={'foo_bar': 'baz'})

    _, kwargs = requests_function.call_args

    assert kwargs['params'] == {'fooBar': 'baz'}


@pytest.mark.parametrize('http_verb', [('post'), ('put'), ('patch')])
def test_passing_requests_params_with_data(mocker, http_verb):
    http_client = HttpClient(hud_client, base_url)
    mocker.patch.object(requests, http_verb)

    # Actual function call, e.g. http_client.get(path, params)
    function_under_test = getattr(http_client, "http_{}".format(http_verb))
    requests_function = getattr(requests, http_verb)

    function_under_test('/test/url',
                        query_params={'foo_bar': 'baz'},
                        data={'fizz_buzz': {'abc': 'jackson_five'}})

    _, kwargs = requests_function.call_args

    assert kwargs['params'] == {'fooBar': 'baz'}
    assert kwargs['json'] == {'fizzBuzz': {'abc': 'jackson_five'}}


def test_jsonifiying(mocker):
    http_client = HttpClient(hud_client, base_url)
    mocker.patch('requests.post')

    timestamp = datetime.now()
    formatted_timestamp = timestamp.isoformat()
    array = ['a', timestamp, 'c']

    http_client.http_post('/test/url',
                          query_params={'timestamp': timestamp},
                          data={
                              'timestamp': timestamp,
                              'array': array
                          })

    _, kwargs = requests.post.call_args

    print(kwargs)

    assert kwargs['params']['timestamp'] == formatted_timestamp
    assert kwargs['json']['timestamp'] == formatted_timestamp
    assert kwargs['json']['array'] == ['a', formatted_timestamp, 'c']


def test_pythonification(mocker):
    http_client = HttpClient(hud_client, base_url)

    mock_response = requests.Response()
    mocker.patch('requests.get').return_value = mock_response
    mocker.patch.object(mock_response, 'json').return_value = {
        'string': 'test-string',
        'boolean': True,
        'number': 123,
        'date': '2017-07-28T15:30:08.176077',
        'array': ['test', '2017-07-28T15:30:08.176077', 123],
        'object': {
            'nestedString': 'test2',
            'nestedDate': '2017-07-28T15:30:08.176077'
        }
    }

    expected_timestamp = datetime(2017, 7, 28, 15, 30, 8, 176077)

    response = http_client.http_get('/test/url')

    assert response['string'] == 'test-string'
    assert response['boolean']
    assert response['number'] == 123
    assert response['date'] == expected_timestamp
    assert response['array'] == ['test', expected_timestamp, 123]
    assert response['object']['nested_string'] == 'test2'
    assert response['object']['nested_date'] == expected_timestamp
