from hudai.resource import Resource
from pydash import pick


class CompanyResource(Resource):
    def __init__(self, secret_key):
        super(secret_key)
        self.resource_name = 'Company'

    def get(self, company_id):
        return self.make_request({
            'method': 'GET',
            'params': {'company_id': company_id},
            'url': '/companies/{company_id}'
        })

    def search(self, params):
        return self.make_request({
            'method': 'GET',
            'params': pick(params, 'company', 'ticket'),
            'url': '/companies'
        })

    def create(self, params):
        return self.make_request({
            'method': 'POST',
            'data': pick(params,'company', 'ticket'),
            'url': '/companies'
        })

    def update(self, params):
        return self.make_request({
            'method': 'PUT',
            'data': pick(params, 'company', 'ticket'),
            'url': '/companies'
        })

    def delete(self, company_id):
        return self.make_request({
            'method': 'DELETE',
            'params': {'company_id': company_id},
            'url': '/companies/{company_id}'
        })
