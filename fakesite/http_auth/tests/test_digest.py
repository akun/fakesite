#!/usr/bin/env python


from tornado.curl_httpclient import CurlAsyncHTTPClient
from tornado.testing import AsyncHTTPTestCase as TestCase

from fakesite.fake_server import get_application


class DigestHandlerTestCase(TestCase):

    def setUp(self):
        super(DigestHandlerTestCase, self).setUp()
        self.http_client = CurlAsyncHTTPClient(self.io_loop,
            defaults=dict(allow_ipv6=False))
    def get_app(self):
        return get_application()

    def test_handler_if_with_auth(self):
        response = self.fetch('/http_auth/digest', auth_mode='digest',
            auth_username='foo', auth_password='bar')
        self.assertEqual(200, response.code)
        self.assertEqual(response.body, b'ok')

    def test_handler_if_without_auth(self):
        response = self.fetch('/http_auth/digest', auth_mode='digest')
        self.assertEqual(401, response.code)
