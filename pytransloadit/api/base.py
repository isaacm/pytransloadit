class APIEndpoint(object):

    def __init__(self, api, endpoint=None, cls=None):
        """API Endpoint base class.

        :param api: - API Client instance
        :type api: TransloadItClient
        :param endpoint: The URI path to the resource
        :type endpoint: str
        """
        self.api = api
        self.endpoint = endpoint
        self._cls = cls

    def get(self, resource_id=None):
        """Gets the details for one or more resources by ID

        :param resource_id: The URI path for the resource
        :type resource_id: str

        :returns: JSON response
        """

        endpoint = self.endpoint

        if resource_id:
            endpoint = '{}/{}'.format(endpoint, resource_id)

        response = self.api.execute(endpoint, method="GET")

        return response

    def post(self, params):
        """ Creates a new instance of the resource.

        :param params: payload for the request

        """
        response = self.api.execute(
            self.endpoint, method="POST", params=params)
        return response

    def put(self, resource):
        """Edits an existing resource.

        :param resource: - The resource instance
        """

        endpoint = self.endpoint

        if resource.id:
            endpoint = '{}/{}'.format(endpoint, resource.id)

        response = self.api.execute(
            endpoint, method="PUT", json=resource.as_json())

        return response

    def delete(self, resource_id):
        """Deletes an existing resource.

        :param resource_id - int - The resource ID to be deleted
        """

        endpoint = '{}/{}'.format(self.endpoint, resource_id)

        response = self.api.execute(endpoint, method="DELETE")

        return response
