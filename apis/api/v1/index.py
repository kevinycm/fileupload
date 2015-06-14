#coding=utf-8
__author__ = 'kevin'

import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template/home.html")


class DisplayHandler(tornado.web.RequestHandler):
    def get(self):
        pass