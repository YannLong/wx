# -*- coding:utf-8 -*-
__author__ = 'longyin'

import tornado.ioloop
import tornado.web


token = "ganji-crm"


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")


class CheckInHandler(object):

    """check in"""

    def get(self):
        signature = get_argument("signature")
        timestamp = get_argument("timestamp")
        nonce = get_argument("nonce")
        echostr = get_argument("echostr")
        self.write(echostr)


handlers = tornado.web.Application([
    (r"/", MainHandler),
    (r"/CheckIn/", CheckInHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
