from tests.unit.pytransloadit import base


class TestTemplates(base.BaseUnitTest):

    def setUp(self):
        super(TestTemplates, self).setUp()

    def test_list_templates_positive(self):
        resp = self.transloadit_api.templates.get()

        self.assertEqual([], resp['items'])
        self.assertEqual(0, resp['count'])

    def test_create_template_positive(self):
        resp = self.transloadit_api.templates.post(
            {
                'name': 'test',
                'template': {
                    'key': 'value'
                }
            }
        )

        self.assertEqual('TEMPLATE_CREATED', resp['ok'])

    def test_get_template_positive(self):
        resp = self.transloadit_api.templates.get('template_id')

        self.assertEqual('template_id', resp['template_id'])

    def test_delete_template_positive(self):
        resp = self.transloadit_api.templates.delete('template_id')

        self.assertEqual('TEMPLATE_DELETED', resp['ok'])

    def test_update_template_positive(self):
        params = {"auth": {"key": ""}}
        resp = self.transloadit_api.templates.update(
            'template_id', params=params)

        self.assertEqual('TEMPLATE_UDPATED', resp['ok'])
