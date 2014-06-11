#!/usr/bin/env python


from tornado.options import define, options, parse_command_line
import tornado.ioloop
import tornado.web

from fakesite.http_auth.basic import BasicHandler
from fakesite.http_auth.digest import DigestAuthHandler


define('port', default=8888, help='run on the given port', type=int)
define('debug', default=False, help='run on the debug mode', type=bool)


def get_application():
    application = tornado.web.Application([
        (r'/http_auth/basic', BasicHandler),
        (r'/http_auth/digest', DigestAuthHandler),
    ], debug=options.debug)
    return application


def main():
    parse_command_line()
    application = get_application()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
