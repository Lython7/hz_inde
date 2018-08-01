import tornado.ioloop
# import tornado.httpserver
import config
from application import Application

if __name__ == '__main__':
    app = Application()
    app.listen(config.options['port'])
    # httpServer = tornado.httpserver.HTTPServer(app)
    # httpServer.bind(config.options['port'])
    # httpServer.start(1)
    try:
        print(' PC端口:%d 服务开启 >>> Program %s start ^_^ <<< ' % (config.options['port'], config.projectName))
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print(' PC端口:%d 服务停止 >>> Program %s stop T_T <<< ' % (config.options['port'], config.projectName))
        tornado.ioloop.IOLoop.current().stop()

