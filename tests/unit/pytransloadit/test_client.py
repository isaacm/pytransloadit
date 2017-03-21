import unittest

from pytransloadit import client
from tests.unit.pytransloadit import base


class TestClient(unittest.TestCase):

    def setUp(self):
        super(TestClient, self).setUp()

    def test_client(self):
        api_client_obj = client.TransloadItClient('auth-key', 'auth-secret')
        self.assertIsNotNone(api_client_obj)

    def test_transloadit_api(self):
        api = client.TransloadItAPI()

        self.assertIsNotNone(api)
        self.assertIsInstance(api.client, client.TransloadItClient)


class TestBilling(base.BaseUnitTest):

    def setUp(self):
        super(TestBilling, self).setUp()

        self.api = client.TransloadItAPI()

    def test_get_monthly_bill(self):
        resp = self.api.bill(month=3, year=2017)

        self.assertEqual('BILL_FOUND', resp['ok'])
