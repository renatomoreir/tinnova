from flask import Flask
from .database import db
from .views import bp as api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(api_bp, url_prefix="/api/veiculos")

    return app
