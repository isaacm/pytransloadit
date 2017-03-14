from pytransloadit import base


class Assemblies(base.APIEndpoint):
    def __init__(self, api, path='/assemblies'):
        """ Creates a new instance of the assemblies API """

        super(Assemblies, self).__init__(api, path=path)

    def get(self, assembly_id=None):
        """Get one or many assemblies.

        Retrieves a list of assemblies when assembly_id is None.

        :param assembly_id: template id to retrieve
        :type assembly_id: str
        """

        return super(Assemblies, self).get(resource_id=assembly_id)

    def post(self, params, files=None):
        """Create a new assembly and sends files for processing.

        :param params: POST data for template creation
        :type params: dict
        :param files: files for the assembly to process
        :type files: list
        """

        return super(Assemblies, self).post(params, files=files)

    def delete(self, assembly_id):
        """Cancel an Assembly.

        :param assembly_id: template id to retrieve
        :type assembly_id: str
        """

        return super(Assemblies, self).delete(assembly_id)

    def replay_assembly(self, assembly_id, params=None):
        """Replay assembly with the given id.

        :param assembly_id: template id to retrieve
        :type assembly_id: str
        :param params: additional params for request
        :type params: dict
        :return:
        """

        path = '{0}/{1}/{2}'.format(self.path, assembly_id, 'replay')
        response = self.api.execute(path, method="POST", params=params)
        return response

    def replay_notification(self, assembly_id, params=None):
        """Replay assembly notification with the given id.

        :param assembly_id: template id to retrieve
        :type assembly_id: str
        :param params: additional params for request
        :type params: dict
        :return:
        """

        path = '{0}/{1}/{2}'.format(
            '/assembly_notifications', assembly_id, 'replay')
        response = self.api.execute(path, method="POST", params=params)
        return response

    def get_notifications(self, params=None):
        """Get a list of assembly notifications.

        :param params: additional params for request
        :type params: dict
        :return:
        """
        path = '/assembly_notifications'

        response = self.api.execute(path, method="GET", params=params)
        return response
