#!/usr/bin/env python3
# /YourFlaskApp/views.py
from models import Planet  # Import the Planet class from the models module

def init_app_routes(app):
    @app.route('/')
    def index():
        return "Welcome to the Planetary API!"

    @app.route('/planet/<string:planet_name>')
    def get_planet_info(planet_name):
        planet = Planet.query.filter_by(name=planet_name.capitalize()).first()
        if planet:
            return f"Planet: {planet.name}, Description: {planet.description}"
        else:
            return "Planet not found", 404
