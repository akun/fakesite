#!/usr/bin/env python


import base64

import tornado


class BasicAuthMixin(object):
    def __request_auth(self, realm):
        if self._headers_written:
            raise Exception('headers have already been written')

        self.set_status(401)
        self.set_header('WWW-Authenticate', 'Basic realm="%s"' % realm)
        self.finish()

        return False

    def get_authenticated_user(self, auth_func, realm):
        """Requests HTTP basic authentication credentials from the client, or
        authenticates the user if credentials are provided."""
        try:
            auth = self.request.headers.get('Authorization')

            if auth == None:
                return self.__request_auth(realm)
            if not auth.startswith('Basic '):
                return self.__request_auth(realm)

            auth_decoded = base64.decodestring(auth[6:])
            username, password = auth_decoded.split(':', 1)

            if auth_func(self, realm, username, password):
                self._current_user = username
                return True
            else:
                return self.__request_auth(realm)
        except Exception:
            return self.__request_auth(realm)


def basic_auth(realm, auth_func):
    """A decorator that can be used on methods that you wish to protect with
    HTTP basic"""
    def basic_auth_decorator(func):
        def func_replacement(self, *args, **kwargs):
            if self.get_authenticated_user(auth_func, realm):
                return func(self, *args, **kwargs)

        return func_replacement
    return basic_auth_decorator


class BasicHandler(BasicAuthMixin, tornado.web.RequestHandler):

    def head(self):
        self.get()

    def get(self):
        if not self.get_authenticated_user(auth_callback, 'realm'):
            return False
        self.write('Hello! I am HTTP Authorization(Basic)')


def auth_callback(request, realm, username, password):
    if username == 'admin' and password == 'admin':
        request.user_id = 1
        return True

    return False
