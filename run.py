import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8787, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = { 
                "/aji/n" : "normal addjavascriptinterface response",
                "/aji/e" : "exploit addjavascriptinterface response"
                }
        self.render("template.html", title="AddJavascriptInterface httpd", items=items)

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/aji/(.*)",tornado.web.StaticFileHandler, {"path": "./"},),
    ],debug=True,autoreload=True,static_hash_cache=False,serve_traceback=True)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port, address='0.0.0.0')
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
