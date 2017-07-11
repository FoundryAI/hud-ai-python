from hudai.resource import Resource
from pydash import pick


class RssFeedMetadataResource(Resource):
    def __init__(self, secret_key):
        super(secret_key)
        self.resource_name = 'RssFeedMetadata'

    def get(self, uuid):
        return self.make_request({
            'method': 'GET',
            'params': {'uuid': uuid},
            'url': '/rss-feed-metadata/{uuid}'
        })

    def search(self, params):
        return self.make_request({
            'method': 'GET',
            'params': pick(params, 'feed_url', 'metadata', 'pulled_at'),
            'url': '/rss-feed-metadata'
        })

    def create(self, params):
        return self.make_request({
            'method': 'POST',
            'data': pick(params, 'data', 'feed_url', 'metadata', 'pulled_at'),
            'url': '/rss-feed-metadata'
        })

    def update(self, params):
        return self.make_request({
            'method': 'PUT',
            'data': pick(params, 'data', 'feed_url', 'metadata', 'pulled_at'),
            'params': pick(params, 'uuid'),
            'url': '/rss-feed-metadata/{uuid}'
        })

    def delete(self, uuid):
        return self.make_request({
            'method': 'DELETE',
            'params': {'uuid': uuid},
            'url': '/rss-feed-metadata/{uuid}'
        })
