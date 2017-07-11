from hudai.resource import Resource
from pydash import pick


class TextCorpusResource(Resource):
    def __init__(self, secret_key):
        super(secret_key)
        self.resource_name = 'TextCorpus'

    def get(self, id):
        return self.make_request({
            'method': 'GET',
            'params': {'id': id},
            'url': '/test-corpora/{id}'
        })

    def search(self, params):
        return self.make_request({
            'method': 'GET',
            'params': pick(params, 'user_id', 'type'),
            'url': '/test-corpora'
        })

    def create(self, params):
        return self.make_request({
            'method': 'POST',
            'data': pick(params, 'user_id', 'type', 'body'),
            'url': '/test-corpora'
        })

    def update(self, params):
        return self.make_request({
            'method': 'PUT',
            'data': pick(params, 'user_id', 'type', 'body'),
            'params': pick(params, 'id'),
            'url': '/test-corpora/{id}'
        })

    def delete(self, id):
        return self.make_request({
            'method': 'DELETE',
            'params': {'id': id},
            'url': '/test-corpora/{id}'
        })
