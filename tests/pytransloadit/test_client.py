import unittest

from pytransloadit import client


class TestClient(unittest.TestCase):

    def setUp(self):
        super(TestClient, self).setUp()

    def test_client(self):
        api_client_obj = client.TransloadItClient('auth-key', 'auth-secret')
        self.assertIsNotNone(api_client_obj)