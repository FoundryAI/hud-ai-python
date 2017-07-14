from hudai.resource import Resource
from pydash import pick


class RssArticleResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client)
        self.resource_name = 'RssArticle'

    def get(self, uuid):
        return self._make_request({
            'method': 'GET',
            'params': {'uuid': uuid},
            'url': '/rss-articles/internal/{uuid}'
        })

    def list(self, params):
        return self._make_request({
            'method': 'GET',
            'params': pick(params, 'feed_url', 'feed_uuid', 'published_at'),
            'url': '/rss-articles/internal'
        })

    def create(self, params):
        return self._make_request({
            'method': 'POST',
            'data': pick(params, 'data', 'feed_url', 'feed_uuid', 'published_at'),
            'url': '/rss-articles/internal'
        })

    def update(self, params):
        return self._make_request({
            'method': 'PUT',
            'data': pick(params, 'data', 'feed_url', 'feed_uuid', 'published_at'),
            'params': pick(params, 'uuid'),
            'url': '/rss-articles/internal/{uuid}'
        })

    def delete(self, uuid):
        return self._make_request({
            'method': 'DELETE',
            'params': {'uuid': uuid},
            'url': '/rss-articles/internal/{uuid}'
        })
