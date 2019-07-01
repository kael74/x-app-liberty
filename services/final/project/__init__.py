# services/users/project/__init__.py

import os  # nuevo
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # nuevo
from flask_debugtoolbar import DebugToolbarExtension  # new
from flask_cors import CORS

# instanciando la db
db = SQLAlchemy()  # nuevo
toolbar = DebugToolbarExtension()  # new
cors = CORS()

# new
def create_app(script_info=None):
    # instanciado la app
    app = Flask(__name__)


# establecer configuraicon
    app_settings = os.getenv('APP_SETTINGS')   # Nuevo
    app.config.from_object(app_settings)       # Nuevo


# set up extensions
    db.init_app(app)
    toolbar.init_app(app)
    cors.init_app(app)

# register blueprints
    from project.api.store import store_blueprint
    app.register_blueprint(store_blueprint)


# shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}
    return app