from tests import base


class TestAssemblies(base.BaseUnitTest):

    def setUp(self):
        super(TestAssemblies, self).setUp()

    def test_list_assemblies_positive(self):
        resp = self.transloadit_api.assemblies.get()

        self.assertEqual([], resp['items'])
        self.assertEqual(0, resp['count'])

    def test_get_assembly_positive(self):
        resp = self.transloadit_api.assemblies.get('assembly_id')

        self.assertEqual('assembly_id', resp['assembly_id'])

    def test_get_assembly_notifications_positive(self):
        resp = self.transloadit_api.assemblies.get_notifications()

        self.assertEqual([], resp['items'])
        self.assertEqual(0, resp['count'])

    def test_cancel_assembly_positive(self):
        resp = self.transloadit_api.assemblies.delete('assembly_id')

        self.assertEqual('ASSEMBLY_CANCELED', resp['ok'])

    def test_replay_assembly_positive(self):
        resp = self.transloadit_api.assemblies.replay_assembly('assembly_id')

        self.assertEqual('ASSEMBLY_REPLAYING', resp['ok'])

    def test_replay_assembly_notification_positive(self):
        resp = self.transloadit_api.assemblies.replay_notification(
            'assembly_id')

        self.assertEqual('ASSEMBLY_NOTIFICATION_REPLAYED', resp['ok'])
