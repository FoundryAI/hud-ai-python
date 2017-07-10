from hudai.resource import Resource
from pydash import pick


class CleanArticleResource(Resource):
    def __init__(self, secret_key):
        super(secret_key)
        self.resource_name = 'CleanArticle'

    def get(self, uuid):
        return self.make_request({
            'method': 'GET',
            'params': {'uuid': uuid},
            'url': '/clean-articles/{uuid}'
        })

    def search(self, params):
        return self.make_request({
            'method': 'GET',
            'params': pick(params, 'article_type', 'description', 'important_score', 'link', 'source', 'title', 'published_at'),
            'url': '/clean-articles'
        })

    def create(self, params):
        return self.make_request({
            'method': 'POST',
            'data': pick(params, 'article_type', 'description', 'important_score', 'link', 'source', 'title', 'published_at'),
            'url': '/clean-articles'
        })

    def update(self, params):
        return self.make_request({
            'method': 'PUT',
            'data': pick(params, 'article_type', 'description', 'important_score', 'link', 'source', 'title', 'published_at'),
            'url': '/clean-articles'
        })

    def delete(self, uuid):
        return self.make_request({
            'method': 'DELETE',
            'params': {'uuid': uuid},
            'url': '/clean-articles/{uuid}'
        })
