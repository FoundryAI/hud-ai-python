from hudai.resource import Resource
from pydash import pick


class UserResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client)
        self.resource_name = 'User'
        self._base_path = '/users'

    def get(self, id):
        return self._make_request({
            'method': 'GET',
            'params': {'id': id},
            'url': '/internal/{id}'
        })

    def list(self, params):
        return self._make_request({
            'method': 'GET',
            'params': pick(params, 'email', 'name'),
            'url': '/internal'
        })

    def create(self, params):
        return self._make_request({
            'method': 'POST',
            'data': pick(params, 'email', 'name', 'hash'),
            'url': '/internal'
        })

    def update(self, params):
        return self._make_request({
            'method': 'PUT',
            'data': pick(params, 'email', 'name', 'hash'),
            'params': pick(params, 'id'),
            'url': '/internal/{id}'
        })

    def delete(self, id):
        return self._make_request({
            'method': 'DELETE',
            'params': {'id': id},
            'url': '/internal/{id}'
        })
