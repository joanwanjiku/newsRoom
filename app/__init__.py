from flask import Flask

from flask_bootstrap import Bootstrap
from config import config_options


bootstrap = Bootstrap()

def create_app(config_name):
    # initialized the app
    app = Flask(__name__, instance_relative_config=True)

    # app configurations
    app.config.from_object(config_options[config_name])
    
    # flask extensions
    bootstrap.init_app(app)

    # register a blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # setup config
    from .requests import configure_request
    configure_request(app)

    return app