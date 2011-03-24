'''
Created on 2011-3-24

@author: liliren
'''

import tornado.httpserver
import tornado.ioloop
import tornado.web

# define one "add" customization funcation which will be used in the assigned template file.
def add(x, y):
    return (x+y)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["item1","item2","item3"]
        # render the corresponding template file, and pass the "**args" to the assigned template
        # not only we can pass the realted parameters, but also can pass the related functions.
        # so extendible and powerful! :)
        self.render("templates/template_test.html", items=items, add=add)


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8081)
    tornado.ioloop.IOLoop.instance().start()
