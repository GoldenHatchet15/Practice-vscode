#!/usr/bin/env python3
from flask import Flask, render_template
from db_setup import db, Planet, create_tables

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    planets = Planet.query.all()  # This should fetch all planets
    return render_template('index.html', planets=planets)

@app.route('/planet/<string:planet_name>')
def get_planet_info(planet_name):
    planet = Planet.query.filter_by(name=planet_name).first()
    if planet:
        return render_template('planet_info.html', planet=planet)
    else:
        return "Planet not found", 404

if __name__ == '__main__':
    create_tables()  # This will create the database tables
    app.run(debug=True)

