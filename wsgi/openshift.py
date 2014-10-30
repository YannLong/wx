# -*- coding:utf-8 -*-
__author__ = 'longyin'


 import tornado.web
 import os

 class MainHandler(tornado.web.RequestHandler):
      def get(self):
           self.render('index.html')

 # Put here yours handlers.

 handlers = [(r'/',MainHandler),]
