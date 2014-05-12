#!/usr/bin/python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8787, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = { 
            "emu-writesd.html" : "write to the sd card through exploit",
            "example1.html" : "default toast example page",
            "id" : "shortlink id.html",
            "id.html" : "print the id of the current user through exploit",
            "ls" : "shortlink ls.html",
            "ls.html" : "list the contents of /storage/sdcard0/Download",
            "ls2" : "shortlink ls2.html",
            "ls2.html" : "list the contents of /mnt/sdcard0/",
            "lsd" : "shortlink lsd.html",
            "lsd.html" : "list the contentes of /mnt/sdcard0/Download useful for after write",
            "n" : "shortlin example1.html",
            "old" : "redundant/working/broken attempts",
            "run.py" : "the server",
            "sms" : "shortlink sms.html",
            "sms.html" : "send sms through exploit",
            "template.html" : "server template",
            "write" : "shortlink emu-writesd.html"
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
