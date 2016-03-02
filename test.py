#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sys.setdefaultencoding() does not exist, here!
import sys

import tornado.ioloop
import tornado.web
import tornado_bz
import test_pg
from tornado.web import RequestHandler

OK = '0'


class test(RequestHandler):
    def get(self, limit=None):
        self.render('test.html')


if __name__ == "__main__":

    web_class = tornado_bz.getAllWebBzRequestHandlers()
    web_class.update(globals().copy())

    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    else:
        port = 9000
    print port

    url_map = tornado_bz.getURLMap(web_class)
    url_map.append((r'/(.*)', test))
    url_map.append((r'/static/(.*)', tornado.web.StaticFileHandler, {'path': "."}))

    settings = tornado_bz.getSettings()
    settings["pg"] = test_pg
    application = tornado.web.Application(url_map, **settings)

    application.listen(port)
    ioloop = tornado.ioloop.IOLoop().instance()

    tornado.autoreload.start(ioloop)
    ioloop.start()
