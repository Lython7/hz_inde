from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def initialize(self):
        pass

    def get(self, *args, **kwargs):
        self.write('lz is good!')

