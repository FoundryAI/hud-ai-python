from hudai.resource import Resource
from pydash import pick


class NewsApiArticleResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client)
        self.resource_name = 'NewsApiArticle'

    def get(self, uuid):
        return self._make_request({
            'method': 'GET',
            'params': {'uuid': uuid},
            'url': '/news-api-articles/internal/{uuid}'
        })

    def list(self, params):
        return self._make_request({
            'method': 'GET',
            'params': pick(params, 'published_at', 'source'),
            'url': '/news-api-articles/internal'
        })

    def create(self, params):
        return self._make_request({
            'method': 'POST',
            'data': pick(params, 'data', 'published_at', 'source'),
            'url': '/news-api-articles/internal'
        })

    def update(self, params):
        return self._make_request({
            'method': 'PUT',
            'data': pick(params, 'data', 'published_at', 'source'),
            'params': pick(params, 'uuid'),
            'url': '/news-api-articles/internal/{uuid}'
        })

    def delete(self, uuid):
        return self._make_request({
            'method': 'DELETE',
            'params': {'uuid': uuid},
            'url': '/news-api-articles/internal/{uuid}'
        })
