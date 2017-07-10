from hudai.resource import Resource
from pydash import pick


class ArticleKeytermResource(Resource):
    def __init__(self, secret_key):
        super(secret_key)
        self.resource_name = 'ArticleKeyterm'

    def get(self, id):
        return self.make_request({
            'method': 'GET',
            'params': {'id': id},
            'url': '/article-keyterms/{id}'
        })

    def search(self, params):
        return self.make_request({
            'method': 'GET',
            'params': pick(params, 'keyterm'),
            'url': '/article-keyterms'
        })

    def create(self, params):
        return self.make_request({
            'method': 'POST',
            'data': pick(params, 'keyterm'),
            'url': '/article-keyterms'
        })
