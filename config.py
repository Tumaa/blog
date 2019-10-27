import os
class Config:
    # BLOG_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'New Blog'
    MAIL_USERNAME="developersjuniors@gmail.com"
    MAIL_PASSWORD="Nairobi001"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://fatuma:qwerty12@localhost/moringas'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get("HEROKU_POSTGRESQL_CHARCOAL_URL")

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
