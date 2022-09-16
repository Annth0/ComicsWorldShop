class Config:
    SECRET_KEY = 'Annth0Koder2022'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB='demo'
    
config = {
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}