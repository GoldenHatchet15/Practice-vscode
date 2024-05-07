#!/usr/bin/env python3
# /YourFlaskApp/__init__.py
from flask import Flask
from .extensions import db
from .models import Planet

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planets.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .views import init_app_routes
    init_app_routes(app)

    return app
