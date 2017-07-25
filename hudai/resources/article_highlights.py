from hudai.resource import Resource


class ArticleHighlightsResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client, base_path='/article-highlights')
        self.resource_name = 'ArticleHighlights'

    def list(self, url_hash=None, user_id=None):
        return self._list(url_hash=url_hash, user_id=user_id)

    def create(self, url=None, user_id=None, body=None):
        return self._create(url=url, user_id=user_id, body=body)

    def get(self, id):
        return self._get(id)

    def update(self, id, body=None):
        return self._update(id, body=body)

    def delete(self, id):
        return self._delete(id)
