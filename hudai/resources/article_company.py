from hudai.resource import Resource
from pydash import pick


class ArticleCompanyResource(Resource):
    def __init__(self, secret_key):
        super(secret_key)
        self.resource_name = 'ArticleCompany'

    def get(self, article_uuid):
        return self.make_request({
            'method': 'GET',
            'params': {'article_uuid': article_uuid},
            'url': '/article-companies/{article_uuid}'
        })

    def search(self, params):
        return self.make_request({
            'method': 'GET',
            'params': pick(params, 'company_id', 'article_type', 'published_at'),
            'url': '/article-companies'
        })

    def create(self, params):
        return self.make_request({
            'method': 'POST',
            'data': pick(params, 'company_id', 'article_type', 'published_at'),
            'url': '/article-companies'
        })
