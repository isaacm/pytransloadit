from vcr_unittest import VCRTestCase

from pytransloadit import client


class BaseUnitTest(VCRTestCase):

    def setUp(self):
        super(BaseUnitTest, self).setUp()

        self.transloadit_client = client.TransloadItClient('auth-key')
        self.transloadit_api = client.TransloadItAPI(
            client=self.transloadit_client)
