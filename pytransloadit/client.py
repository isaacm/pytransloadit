from datetime import datetime
from datetime import timedelta
import hashlib
import hmac
import json

import requests

from pytransloadit.api import assemblies
from pytransloadit.api import templates

DEFAULT_BASE_URL = 'https://api2.transloadit.com'


class TransloadItClient(object):
    """HTTP REST client for transloadit APIs."""

    def __init__(self, key, secret,
                 duration=300,
                 max_size=None,
                 base_url=DEFAULT_BASE_URL, **kwargs):
        self.key = key
        self.secret = secret
        self.duration = duration
        self.max_size = max_size
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Python Transloadit 0.0.0'
        }
        self._client_kwargs = kwargs

    def _sign_request(self, params):
        return hmac.new(
            self.secret, json.dumps(params), hashlib.sha1).hexdigest()

    def build_payload(self, params):
        data = {}
        expires_dt = datetime.utcnow() + timedelta(seconds=self.duration)

        if 'auth' not in params:
            params['auth'] = {
                'key': self.key,
                'expires': expires_dt.strftime('%Y/%m/%d %H:%M:%S+00:00')
            }

        if self.max_size is not None:
            params['auth']['max_size'] = self.max_size

        data['params'] = json.dumps(params)
        data['signature'] = self._sign_request(params)
        return data

    def execute(self, path, method='GET', params=None, files=None):
        url = "{}{}".format(self.base_url, path)

        if params is None:
            params = {}

        data = self.build_payload(params)

        if method.upper() in ['POST', 'PUT', 'DELETE']:
            req_kwargs = {'data': data}
        else:
            req_kwargs = {'params': data}

        response = requests.request(
            method,
            url,
            files=files,
            headers=self.headers,
            **req_kwargs
        )
        return response.json()


class TransloadIt(object):
    def __init__(self, client=None, key=None, secret=None, **kwargs):

        if client is None:
            client = TransloadItClient(key, secret, **kwargs)

        self.client = client
        self.assemblies = assemblies.Assemblies(self.client)
        self.templates = templates.Templates(self.client)

    def bill(self, month=None, year=None):
        now = datetime.utcnow()
        if month is None:
            month = now.strftime('%m')

        if year is None:
            year = now.strftime('%Y')

        return self.client.execute('/bill/{0}-{1:02d}'.format(year, month))
