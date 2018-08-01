import os

BASE_DIR = os.path.dirname(__file__)

projectName = 'TEST'

options = {
    'port': 8888,
}

settings = {
    'static_path': os.path.join(BASE_DIR, 'static'),
    'template_path': os.path.join(BASE_DIR, 'templates'),
    'debug': True,
}

# settings = dict(
#     debug=True,  # 设置debug启动方式
#     static_path=os.path.join(BASE_DIR, 'static'),
#     template_path=os.path.join(BASE_DIR, 'templates'),
    # login_url="/login",  #重定向到登录页面
    # packet的配置
    # pycket ={
    #     "engine": "redis",  # 配置存储类型
    #     "storage": {
    #         "host": "localhost",
    #         "port": 6379,
    #         "db_sessions": 5,
    #         "db_notifications": 11,
    #         "max_connections": 2 ** 31
    #     },
    #     "cookies": {
    #         "expires_days": 30,
    #         "max_age": 360
    #     }
    # },
    # cookie_secret="aaa",
    # xscf_cookies=True
# )