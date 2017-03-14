from pytransloadit import base


class Templates(base.APIEndpoint):
    def __init__(self, api, path='/templates'):
        super(Templates, self).__init__(api, path=path)

    def get(self, template_id=None):
        """Get one or many templates.

        Retrieves a list of templates when template_id is None.

        :param template_id: template id to retrieve
        :type template_id: str
        """

        return super(Templates, self).get(resource_id=template_id)

    def post(self, params):
        """Create a new template.

        :param params: POST data for template creation
        :type params: dict
        """

        return super(Templates, self).post(params)

    def delete(self, template_id):
        """Delete a template with the given id.

        :param template_id: template id to retrieve
        :type template_id: str
        """

        return super(Templates, self).delete(template_id)

    def update(self, template_id, params):
        """Edit a template with the given id.

        :param template_id: template id to retrieve
        :type template_id: str
        :param params: payload for the request
        :type params: dict
        """

        return super(Templates, self).put(template_id, params)
