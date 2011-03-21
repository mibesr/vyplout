#!/usr/bin/python
# -*- coding: utf-8 -*-
"""web main"""

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

#from rockps.auth import AuthHandler


class MainHandler(RequestHandler):
    def get(self):
        self.write("hello world")
        
settings = {
}

application = Application([(r"/", MainHandler), ], **settings)

if __name__ == "__main__":
    http_server = HTTPServer(application)
    http_server.listen(8081)
    IOLoop.instance().start()
