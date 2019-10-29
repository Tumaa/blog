import os
class Config:
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'New Blog'
    MAIL_USERNAME="developersjuniors@gmail.com"
    MAIL_PASSWORD="Nairobi001"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUG = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://fatuma:qwerty12@localhost/moringas'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
