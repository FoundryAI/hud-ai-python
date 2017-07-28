from ..resource import Resource


class UserResource(Resource):
    def __init__(self, client):
        Resource.__init__(self, client, base_path='/users')
        self.resource_name = 'User'

    # Core CRUD Actions


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


    # Convenience management of their tracked KeyTerms


    def tracked_terms_list(self, id):
        return self.get('/{id}/tracked-terms',
                        params={'id': id})

    def tracked_terms_add(self, id, term):
        return self.post('/{id}/tracked-terms',
                         params={'id': id},
                         data={'term': term})

    def tracked_terms_remove(self, id, term):
        return self.delete('/{id}/tracked-terms/{term}',
                           params={'id': id, 'term': term})


    # Convenience management of their tracked Companies


    def tracked_companies_list(self, id):
        return self.get('/{id}/tracked-companies', params={'id': id})

    def tracked_companies_add(self, id, company_id):
        return self.post('/{id}/tracked-companies',
                         params={'id': id},
                         data={'company_id': company_id})

    def tracked_companies_remove(self, user_id, company_id):
        return self.delete('/{user_id}/tracked-companies/{company_id}',
                           params={'user_id': user_id, 'company_id': company_id})
