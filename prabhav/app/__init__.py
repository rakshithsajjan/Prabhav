from flask import Flask
from app.config import load_configurations, configure_logging
from .views import webhook_blueprint, analytics_blueprint


def create_app():
    app = Flask(__name__)
    # set the route
    # app.config["APPLICATION_ROOT"] = "/backend"
    # Load configurations and logging settings
    load_configurations(app)
    configure_logging()

    # Import and register blueprints, if any
    app.register_blueprint(webhook_blueprint)
    app.register_blueprint(analytics_blueprint)

    return app
