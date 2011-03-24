'''
Created on 2011-3-22

@author: liliren
'''
import tornado.httpserver  
import tornado.ioloop  
import tornado.web

settings = {'debug' : True}

class MainHandler(tornado.web.RequestHandler):  
    def get(self):  
        return

application = tornado.web.Application([
     (r"/", MainHandler),
     ], **settings)

def main():
    server = tornado.httpserver.HTTPServer(application)
    server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()