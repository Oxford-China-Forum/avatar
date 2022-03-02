import os


class Config:
    '''Common configurations.'''

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    LOG_DIR = os.path.join(BASE_DIR, 'log')
    UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')
    THREADS_PER_PAGE = 2
    CSRF_ENABLED = True
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ocf.db'


class DevelopmentConfig(Config):
    '''Development configurations.'''

    ENV = 'development'
    TESTING = True
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SCHEDULER_API_ENABLED = True
    ALLOWED_ORIGINS = [] # Disable CORS


class ProductionConfig(Config):
    '''Production configurations.'''

    ENV = 'production'
    TESTING = False
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEDULER_API_ENABLED = False
    ALLOWED_ORIGINS = ['http://2022.oxchina.org', 'https://2022.oxchina.org', 'http://2022.oxchina.net', 'https://2022.oxchina.net', 'http://ocf.georgeyu.cn', 'https://ocf.georgeyu.cn']


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
