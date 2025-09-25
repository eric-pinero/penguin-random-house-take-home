from flask import Flask
from app.config.config import Config
from app.extensions import db, migrate, ma

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    # Register blueprints
    from app.routes.incidents import incidents_bp
    app.register_blueprint(incidents_bp)

    return app