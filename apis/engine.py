__author__ = 'kevin'

import os, sys
import os.path

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, os.pardir))

from base.settings import load_settings
load_settings('base', 'apis', 'libs')

from settings import load_tornado_settings

from tornado.options import options, define, parse_command_line
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.wsgi


from api.v1.filetrans import UploadHandler, DownloadHandler
from api.v1.index import HomeHandler, DisplayHandler

define('port', type=int, default=9999)

application = tornado.web.Application([
    (r"/", HomeHandler),
    (r"/file/all", DisplayHandler),
    (r"/file/upload", UploadHandler),
    (r"/file/download", DownloadHandler)
], **(load_tornado_settings(PROJECT_ROOT)))

if __name__ == "__main__":
    parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application, no_keep_alive=True, xheaders=True, max_body_size=200 * 1024 * 1024 * 1024)
    http_server.bind(options.port)
    http_server.start()
    tornado.ioloop.IOLoop.instance().start()