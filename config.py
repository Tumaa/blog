import os

class Config:
   '''
   General configuration parent class
   '''
   pass
   # simple mde  configurations
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://fatuma:qwerty12@localhost/moringas'
   #  email configurations
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

   
class ProdConfig(Config):
   '''
   Production  configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   pass
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://fatuma:qwerty12@localhost/moringas'
class DevConfig(Config):
   '''
   Development  configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://fatuma:qwerty12@localhost/moringas'
   DEBUG = True
   
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}