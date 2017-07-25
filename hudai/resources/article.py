from hudai.resource import Resource


class ArticleResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client, base_path='/articles')
        self.resource_name = 'Article'

    def list(self, article_type=None, published_after=None, published_before=None):
        return self._list(
            article_type=article_type,
            published_after=published_after,
            published_before=published_before
        )

    def create(self, article_type=None, importance_score=None, published_at=None, raw_location=None):
        return self._create(
            article_type=article_type,
            importance_score=importance_score,
            published_at=published_at,
            raw_location=raw_location
        )

    def get(self, id):
        return self._get(id)

    def update(self, id, article_type=None, importance_score=None, published_at=None, raw_location=None):
        return self._update(id,
            article_type=article_type,
            importance_score=importance_score,
            published_at=published_at,
            raw_location=raw_location
        )

    def delete(self, id):
        return self._delete(id)

    def key_terms(self, id):
        return self.get('/{id}/key-terms', {
            'params': {'id': id}
        })
