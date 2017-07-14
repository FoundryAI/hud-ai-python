from hudai.resource import Resource
from pydash import pick


class TaskResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client)
        self.resource_name = 'Task'

    def get(self, uuid):
        return self._make_request({
            'method': 'GET',
            'params': {'uuid': uuid},
            'url': '/tasks/internal/{uuid}'
        })

    def create(self, params):
        return self._make_request({
            'method': 'POST',
            'data': pick(params, 'uuid'),
            'url': '/tasks/internal'
        })

    def delete(self, uuid):
        return self._make_request({
            'method': 'DELETE',
            'params': {'uuid': uuid},
            'url': '/tasks/internal/{uuid}'
        })
