from hudai.resource import Resource
from pydash import pick


class RelevantArticleResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client)
        self.resource_name = 'RelevantArticle'

    def list(self, params):
        return self._make_request({
            'method': 'GET',
            'params': pick(params, 'user', 'scored_at'),
            'url': '/relevant-articles/internal'
        })

    def create(self, params):
        return self._make_request({
            'method': 'POST',
            'data': pick(params, 'user', 'scored_at', 'relevant_articles'),
            'url': '/relevant-articles/internal'
        })

    def update(self, params):
        return self._make_request({
            'method': 'PUT',
            'data': pick(params, 'scored_at', 'relevant_articles'),
            'params': pick(params, 'user'),
            'url': '/relevant-articles/internal/{user}'
        })

    def delete(self, user):
        return self._make_request({
            'method': 'DELETE',
            'params': {'user': user},
            'url': '/relevant-articles/internal/{user}'
        })
