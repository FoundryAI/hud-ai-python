from hudai.resource import Resource
from pydash import pick


class RelevantArticleResource(Resource):
    def __init__(self, secret_key):
        super(secret_key)
        self.resource_name = 'RelevantArticle'

    def search(self, params):
        return self.make_request({
            'method': 'GET',
            'params': pick(params, 'user', 'scored_at'),
            'url': '/relevant-articles'
        })

    def create(self, params):
        return self.make_request({
            'method': 'POST',
            'data': pick(params, 'user', 'scored_at', 'relevant_articles'),
            'url': '/relevant-articles'
        })

    def update(self, params):
        return self.make_request({
            'method': 'PUT',
            'data': pick(params, 'scored_at', 'relevant_articles'),
            'params': pick(params, 'user'),
            'url': '/relevant-articles/{user}'
        })

    def delete(self, user):
        return self.make_request({
            'method': 'DELETE',
            'params': {'user': user},
            'url': '/relevant-articles/{user}'
        })
