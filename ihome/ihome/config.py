class Config(object):
    """配置信息"""
    DEBUG = True
    SECRET_KEY = "lq942966"

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:123@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis 配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask-session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SINGER = True  # 对cookie中的session_id进行隐藏处理
    PERMAENT_SESSION_LIFETIME = 86400  # session数据的有效期，单位秒


class DevelopmentConfig(Config):
    """开发模式配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置信息"""


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig

}
