#!/usr/bin/env python


from tornado.testing import AsyncHTTPTestCase as TestCase

from fakesite.fake_server import get_application


class BasicHandlerTestCase(TestCase):

    def get_app(self):
        return get_application()

    def test_handler_if_with_auth(self):
        response = self.fetch('/http_auth/basic', auth_username='admin',
            auth_password='admin')
        self.assertEqual(200, response.code)
        self.assertEqual(b'Hello! I am HTTP Authorization(Basic)',
            response.body)

    def test_handler_if_without_auth(self):
        response = self.fetch('/http_auth/basic')
        self.assertEqual(401, response.code)
