from hudai.resource import Resource


class SystemEventResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client, base_path='/system-events')
        self.resource_name = 'SystemEvent'

    def list(self):
        return self._list()

    def create(self, event_name=None, event_payload=None):
        return self._create(event_name=event_name, event_payload=event_payload)

    def get(self, id):
        return self._get(id)

    def update(self, id, event_name=None, event_payload=None):
        return self._update(id, event_name=event_name, event_payload=event_payload)

    def delete(self, domain):
        return self._delete(id)
