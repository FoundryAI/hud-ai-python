from hudai.resource import Resource


class UserResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client, base_path='/users')
        self.resource_name = 'User'

    def list(self, email=None, name=None):
        return self._list(email=email, name=name)

    def create(self, email=None, name=None, password_hash=None):
        return self._create(email=email, name=name, password_hash=password_hash)

    def get(self, id):
        return self._get(id)

    def update(self, id, email=None, name=None, password_hash=None):
        return self._update(id, email=email, name=name, password_hash=password_hash)

    def delete(self, id):
        return self._delete(id)
