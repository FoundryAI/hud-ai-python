from ..resource import Resource


class ArticleHighlightsResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client, base_path='/article-highlights')
        self.resource_name = 'ArticleHighlights'

    def list(self, link_hash=None, user_id=None):
        return self._list(link_hash=link_hash, user_id=user_id)

    def create(self, article_id=None, user_id=None, body=None):
        return self._create(article_id=article_id, user_id=user_id, body=body)

    def get(self, id):
        return self._get(id)

    def update(self, id, body=None):
        return self._update(id, body=body)

    def delete(self, id):
        return self._delete(id)
