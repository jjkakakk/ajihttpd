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
            "aji/emu-writesd.html" : "write to the sd card through exploit",
            "aji/example1.html" : "default toast example page",
            "aji/id" : "shortlink id.html",
            "aji/id.html" : "print the id of the current user through exploit",
            "aji/ls" : "shortlink ls.html",
            "aji/ls.html" : "list the contents of /storage/sdcard0/Download",
            "aji/ls2" : "shortlink ls2.html",
            "aji/ls2.html" : "list the contents of /mnt/sdcard0/",
            "aji/lsd" : "shortlink lsd.html",
            "aji/lsd.html" : "list the contents of /mnt/sdcard0/Download useful for after write",
            "aji/n" : "shortlin example1.html",
            "aji/old" : "redundant/working/broken attempts",
            "aji/run.py" : "the server",
            "aji/sms" : "shortlink sms.html",
            "aji/sms.html" : "send sms through exploit",
            "aji/template.html" : "server template",
            "aji/write" : "shortlink emu-writesd.html"
            }
        self.render("template.html", title="AddJavascriptInterface httpd", items=items)

def main():
    tornado.options.parse_command_line()
    print "default port is 8787. hubert.\n"
    print "load up the vulnerable android app and point it at this server...\n";
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/aji/(.*)",tornado.web.StaticFileHandler, {"path": "./"},),
    ],debug=True,autoreload=True,static_hash_cache=False,serve_traceback=True)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port, address='0.0.0.0')
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
