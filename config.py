class Config:
    SECRET_KEY = 'Annth0Koder2022'

class DevelopmentConfig(Config):
    DEBUG = True
    
config = {
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}