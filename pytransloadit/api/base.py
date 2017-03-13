class APIEndpoint(object):

    def __init__(self, api, path=None, cls=None):
        """API Endpoint base class.

        :param api: - API Client instance
        :type api: TransloadItClient
        :param path: The URI path to the resource
        :type path: str
        """
        self.api = api
        self.path = path
        self._cls = cls

    def get(self, resource_id=None):
        """Gets the details for one or more resources by ID

        :param resource_id: The URI path for the resource
        :type resource_id: str

        :returns: JSON response
        """

        path = self.path

        if resource_id:
            path = '{}/{}'.format(path, resource_id)

        response = self.api.execute(path, method="GET")

        return response

    def post(self, params):
        """ Creates a new instance of the resource.

        :param params: payload for the request

        """
        response = self.api.execute(
            self.path, method="POST", params=params)
        return response

    def put(self, resource):
        """Edits an existing resource.

        :param resource: - The resource instance
        """

        path = self.path

        if resource.id:
            path = '{}/{}'.format(path, resource.id)

        response = self.api.execute(
            path, method="PUT", json=resource.as_json())

        return response

    def delete(self, resource_id):
        """Deletes an existing resource.

        :param resource_id - int - The resource ID to be deleted
        """

        path = '{}/{}'.format(self.path, resource_id)

        response = self.api.execute(path, method="DELETE")

        return response
