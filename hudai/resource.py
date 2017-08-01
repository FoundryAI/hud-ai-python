from pydash import omit

from .error import HudAiError


class Resource(object):
    """
    Inheritable class to build out the actions that can be taken at a particular
    endpoint (e.g. /my-resource)
    Includes:
        - all standard HTTP verbs as via `http_VERB` e.g. `http_get`
        - helper methods for the standard CRUD actions
    """
    def __init__(self, client, base_path=''):
        """
        :param client: API client
        """

        if client is None:
            raise HudAiError('client required', 'initialization_error')

        self._client = client
        self._base_path = base_path


    # Standard HTTP Verbs with url params injected into the given paths


    def http_get(self, path, **request_params):
        """
        Wrapped HTTP action that
            - builds off the base path
            - pulls apart the query params from the URL params
        """
        full_path = self._build_path(path, request_params.get('params'))

        client_params = omit(request_params, 'params')

        return self._client.http_get(full_path, **client_params).json()


    def http_post(self, path, **request_params):
        """
        Wrapped HTTP action that
            - builds off the base path
            - pulls apart the query params from the URL params
        """
        full_path = self._build_path(path, request_params.get('params'))

        client_params = omit(request_params, 'params')

        return self._client.http_post(full_path, **client_params).json()


    def http_put(self, path, **request_params):
        """
        Wrapped HTTP action that
            - builds off the base path
            - pulls apart the query params from the URL params
        """
        full_path = self._build_path(path, request_params.get('params'))

        client_params = omit(request_params, 'params')

        return self._client.http_put(full_path, **client_params).json()


    def http_patch(self, path, **request_params):
        """
        Wrapped HTTP action that
            - builds off the base path
            - pulls apart the query params from the URL params
        """
        full_path = self._build_path(path, request_params.get('params'))

        client_params = omit(request_params, 'params')

        return self._client.http_patch(full_path, **client_params).json()


    def http_delete(self, path, **request_params):
        """
        Wrapped HTTP action that
            - builds off the base path
            - pulls apart the query params from the URL params
        """
        full_path = self._build_path(path, request_params.get('params'))

        client_params = omit(request_params, 'params')

        return self._client.http_delete(full_path, **client_params).json()


    # CRUD actions common to many endpoints


    def _list(self, **query_params):
        return self.http_get('/', query_params=query_params)

    def _create(self, **data):
        return self.http_post('/', data=data)

    def _fetch(self, entity_id):
        return self.http_get('/{id}', params={'id': entity_id})

    def _update(self, entity_id, **data):
        return self.http_put('/{id}', params={'id': entity_id}, data=data)

    def _delete(self, entity_id):
        return self.http_delete('/{id}', params={'id': entity_id})


    # Helper functions


    def _build_path(self, url, query_params):
        """
        Build the url path string
        :return url:
        """
        path = "{}{}".format(self._base_path, url)

        if not query_params:
            return path

        return path.format(**query_params)
