import tornado.web
from views import index
import config

# 路由配置
urls = [
    (r'/', index.IndexHandler),
]

class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(urls, **config.settings)