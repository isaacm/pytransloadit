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

    def post(self, params, files=None):
        """ Creates a new instance of the resource.

        :param params: payload for the request
        :type params: dict
        :param files: a list of files to process
        :type files: list of strings
        """

        response = self.api.execute(
            self.path, method="POST", params=params, files=files)
        return response

    def put(self, resource_id, params):
        """Edits an existing resource.

        :param resource_id: - The resource identifier to make edit
        :type resource_id: str
        :param params: payload for the request
        :type params: dict
        """

        path = '{0}/{1}'.format(self.path, resource_id)

        response = self.api.execute(path, method="PUT", params=params)

        return response

    def delete(self, resource_id):
        """Deletes an existing resource.

        :param resource_id - int - The resource ID to be deleted
        """

        path = '{}/{}'.format(self.path, resource_id)

        response = self.api.execute(path, method="DELETE")

        return response
