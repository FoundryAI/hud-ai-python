from ..resource import Resource


class UserResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client, base_path='/users')
        self.resource_name = 'User'

    def list(self, email=None):
        return self._list(email=email)

    def create(self, email=None, name=None):
        return self._create(email=email, name=name)

    def get(self, id):
        return self._get(id)

    def update(self, id, email=None, name=None):
        return self._update(id, email=email, name=name)

    def delete(self, id):
        return self._delete(id)
