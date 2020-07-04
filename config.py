import os

class Config:
    
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfg(Config):
    """
    configurations for prod environment inherits from Config
    """
    pass

class DevConfig(Config):
    """
    configurations for dev environment inherits from Config
    """
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfg
}