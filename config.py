class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:Frankline@localhost/new_app_db"
    SLQALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True