from flask import Flask


def createa_app():
    """ Initialize the core application """
    app = Flask(__name__, instance_relative_config=False)
    with app.app_context():
        # Include essential parts
        from .ai_api import ai_api
        from .scraper_api import scraper_api
        # Register Blueprints
        app.register_blueprint(ai_api.ai_api_bp)
        app.register_blueprint(scraper_api.scraper_api_bp)
        return app
