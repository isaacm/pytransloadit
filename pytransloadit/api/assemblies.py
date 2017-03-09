from pytransloadit.api import base


class Assemblies(base.APIEndpoint):
    def __init__(self, api, endpoint='/assemblies'):
        """ Creates a new instance of the assemblies API """

        super(Assemblies, self).__init__(api, endpoint=endpoint)

    def get(self, assembly_id=None):
        """Get one or many assemblies.

        Retrieves a list of assemblies when assembly_id is None.

        :param assembly_id: template id to retrieve
        :type assembly_id: str
        """

        return super(Assemblies, self).get(resource_id=assembly_id)

    def post(self, params):
        """Create a new assembly.

        :param params: POST data for template creation
        :type params: dict
        """

        return super(Assemblies, self).post(params)

    def delete(self, assembly_id):
        """Cancel an Assembly.

        :param assembly_id: template id to retrieve
        :type assembly_id: str
        """

        return super(Assemblies, self).delete(assembly_id)

    def replay_assembly(self, assembly_id, params):
        """Replay assembly with the given id.

        :param assembly_id: template id to retrieve
        :type assembly_id: str
        :param params: additional params for request
        :type params: dict
        :return:
        """

        url = '{0}/{1}/{2}'.format(self.endpoint, assembly_id, 'replay')
        response = self.api.execute("POST", url, params=params)
        return response

    def replay_notification(self, assembly_id, params):
        """Replay assembly notification with the given id.

        :param assembly_id: template id to retrieve
        :type assembly_id: str
        :param params: additional params for request
        :type params: dict
        :return:
        """

        url = '{0}/{1}/{2}'.format(
            '/assembly_notifications', assembly_id, 'replay')
        response = self.api.execute("POST", url, params=params)
        return response

    def get_notifications(self, params):
        """Get a list of assembly notifications.

        :param params: additional params for request
        :type params: dict
        :return:
        """
        endpoint = '/assembly_notifications'

        response = self.api.execute("GET", endpoint, params)
        return response.json()
