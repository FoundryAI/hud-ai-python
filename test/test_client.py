"""HUD.ai Client Specs

Makes sure that the client surfaces the right resources and performs the
required token exchanges
"""

from datetime import datetime, timedelta
import pytest
import requests

from hudai.client import Client
from hudai.error import HudAiError
from hudai.resources import *


mock_client_id = '7fe475ee-aae1-4ff2-82f4-ab48948edad0'
mock_client_secret = '42202699-d526-4505-9218-28e2af284e70'
mock_redirect_uri = 'https://app.example.com/auth/callbacks/hud-ai'

def test_initialization():
    client = Client(client_id=mock_client_id)

    assert isinstance(client, Client)
    assert isinstance(client.article_highlights, ArticleHighlightsResource)
    assert isinstance(client.article_key_term, ArticleKeyTermResource)
    assert isinstance(client.article, ArticleResource)
    assert isinstance(client.company_key_term, CompanyKeyTermResource)
    assert isinstance(client.company, CompanyResource)
    assert isinstance(client.domain, DomainResource)
    assert isinstance(client.key_term, KeyTermResource)
    assert isinstance(client.system_event, SystemEventResource)
    assert isinstance(client.system_task, SystemTaskResource)
    assert isinstance(client.text_corpus, TextCorpusResource)
    assert isinstance(client.user_company, UserCompanyResource)
    assert isinstance(client.user_key_term, UserKeyTermResource)
    assert isinstance(client.user, UserResource)


def test_get_authorize_uri_without_redirect_uri():
    client = Client(client_id=mock_client_id)

    with pytest.raises(HudAiError):
        client.get_authorize_uri()


def test_get_authorize_uri():
    redirect_uri = 'https://app.example.com/auth/callbacks/hud-ai'
    client = Client(client_id=mock_client_id, redirect_uri=redirect_uri)

    expected_uri = (
        'https://auth.hud.ai/oauth2/authorize' +
        '?response_type=code' +
        '&client_id={client_id}' +
        '&redirect_uri={redirect_uri}'
    ).format(client_id=mock_client_id, redirect_uri=redirect_uri)

    assert client.get_authorize_uri() == expected_uri


def test_refresh_tokens_valid_token(mocker):
    client = Client(client_id=mock_client_id)
    client.token_expires_at = datetime.now() + timedelta(hours=1)

    mocker.spy(client, '_refresh_tokens')

    client.refresh_tokens()

    assert client._refresh_tokens.call_count == 0


def test_refresh_tokens_expired_token(mocker):
    client = Client(client_id=mock_client_id, client_secret=mock_client_secret)

    mock_refresh_token = 'mock-refresh-token'

    client.token_expires_at = datetime.now() - timedelta(hours=1)
    client.refresh_token = mock_refresh_token

    mock_response = mocker.Mock()
    mock_json = {
        'access_token': 'new-token',
        'refresh_token': 'new-refresh-token',
        'expires_in': 100000
    }
    mock_response.json.return_value = mock_json

    mocker.patch('requests.post', return_value=mock_response)

    client.refresh_tokens()

    request_args, request_kwargs = requests.post.call_args

    assert request_args[0] == 'https://auth.hud.ai/oauth2/token'
    assert request_kwargs['json'] == {
        'client_id': mock_client_id,
        'client_secret': mock_client_secret,
        'grant_type': 'refresh_token',
        'refresh_token': mock_refresh_token
    }
    assert client.access_token == mock_json['access_token']
    assert client.refresh_token == mock_json['refresh_token']

    projected_expiration = datetime.now() + \
        timedelta(milliseconds=mock_json['expires_in'])

    assert (
        (projected_expiration - timedelta(seconds=1))
        < client.token_expires_at <
        (projected_expiration + timedelta(seconds=1))
    )


def test_refresh_tokens_auth_code(mocker):
    client = Client(
        client_id=mock_client_id,
        client_secret=mock_client_secret,
        redirect_uri=mock_redirect_uri
    )

    mock_auth_code = 'mock-auth-code'

    client.set_auth_code(mock_auth_code)

    mock_response = mocker.Mock()
    mock_json = {
        'access_token': 'new-token',
        'refresh_token': 'new-refresh-token',
        'expires_in': 100000
    }
    mock_response.json.return_value = mock_json

    mocker.patch('requests.post', return_value=mock_response)

    client.refresh_tokens()

    request_args, request_kwargs = requests.post.call_args

    assert request_args[0] == 'https://auth.hud.ai/oauth2/token'
    assert request_kwargs['json'] == {
        'client_id': mock_client_id,
        'client_secret': mock_client_secret,
        'grant_type': 'authorization_code',
        'code': mock_auth_code,
        'redirect_uri': mock_redirect_uri
    }
    assert client.access_token == mock_json['access_token']
    assert client.refresh_token == mock_json['refresh_token']

    projected_expiration = datetime.now() + \
        timedelta(milliseconds=mock_json['expires_in'])

    assert (
        (projected_expiration - timedelta(seconds=1))
        < client.token_expires_at <
        (projected_expiration + timedelta(seconds=1))
    )


def test_refresh_tokens_client_credentials(mocker):
    client = Client(client_id=mock_client_id, client_secret=mock_client_secret)

    mock_response = mocker.Mock()
    mock_json = {
        'access_token': 'new-token',
        'refresh_token': 'new-refresh-token',
        'expires_in': 100000
    }
    mock_response.json.return_value = mock_json

    mocker.patch('requests.post', return_value=mock_response)

    client.refresh_tokens()

    request_args, request_kwargs = requests.post.call_args

    assert request_args[0] == 'https://auth.hud.ai/oauth2/token'
    assert request_kwargs['json'] == {
        'client_id': mock_client_id,
        'client_secret': mock_client_secret,
        'grant_type': 'client_credentials'
    }
    assert client.access_token == mock_json['access_token']
    assert client.refresh_token == mock_json['refresh_token']

    projected_expiration = datetime.now() + \
        timedelta(milliseconds=mock_json['expires_in'])

    assert (
        (projected_expiration - timedelta(seconds=1))
        < client.token_expires_at <
        (projected_expiration + timedelta(seconds=1))
    )
