from flask import Flask

from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    # app configurations
    
    # flask extensions
    bootstrap.init_app(app)


    return app