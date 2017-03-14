import inspect
import os

from vcr_unittest import VCRTestCase

from pytransloadit import client


class BaseUnitTest(VCRTestCase):

    def setUp(self):
        super(BaseUnitTest, self).setUp()

        self.transloadit_client = client.TransloaditClient(
            'auth-key', 'auth-secret')
        self.transloadit_api = client.TransloadIt(
            client=self.transloadit_client)

    def _get_cassette_library_dir(self):
        test_dir = os.path.dirname(inspect.getfile(self.__class__))
        return os.path.join(test_dir, 'fixtures', 'cassettes')
