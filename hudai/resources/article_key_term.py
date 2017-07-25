from hudai.resource import Resource


class ArticleKeyTermResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client, base_path='/article-key-terms')
        self.resource_name = 'ArticleKeyTerm'

    def list(self, article_id=None, published_after=None, published_before=None, term=None):
        return self._list(
            article_id=article_id,
            published_after=published_after,
            published_before=published_before,
            term=term
        )

    def create(self, term=None, article_id=None, published_at=None):
        return self._create(term=term, article_id=article_id, published_at=published_at)

    def get(self, id):
        return self._get(id)

    def delete(self, id):
        return self._delete(id)
