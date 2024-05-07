#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)

# Data about planets stored in a dictionary
planets_info = {
    'Mercury': {
        'description': 'Mercury is the closest planet to the Sun and due to its proximity, it is not easily seen except during twilight...',
        'distance_from_sun': '57.91 million km',
        'orbit_period': '88 days'
    },
    'Venus': {
        'description': 'Venus is the second planet from the Sun and is Earth’s closest planetary neighbor...',
        'distance_from_sun': '108.2 million km',
        'orbit_period': '225 days'
    },
    'Earth': {
        'description': 'Earth is the third planet from the Sun and the only astronomical object known to harbor life...',
        'distance_from_sun': '149.6 million km',
        'orbit_period': '365.25 days'
    },
    'Mars': {
        'description': 'Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System...',
        'distance_from_sun': '227.9 million km',
        'orbit_period': '687 days'
    },
    'Jupiter': {
        'description': 'Jupiter is the largest planet in the Solar System and is known for its prominent Great Red Spot...',
        'distance_from_sun': '778.5 million km',
        'orbit_period': '4333 days'
    },
    'Saturn': {
        'description': 'Saturn is the sixth planet from the Sun and the second-largest in the Solar System...',
        'distance_from_sun': '1.434 billion km',
        'orbit_period': '10759 days'
    },
    'Uranus': {
        'description': 'Uranus is the seventh planet from the Sun. It has the coldest planetary atmosphere in the Solar System...',
        'distance_from_sun': '2.871 billion km',
        'orbit_period': '30688 days'
    },
    'Neptune': {
        'description': 'Neptune is the eighth and farthest known planet from the Sun in the Solar System...',
        'distance_from_sun': '4.495 billion km',
        'orbit_period': '60182 days'
    },
    'Moon': {
        'description': 'The Moon is Earth\'s only permanent natural satellite. It is the fifth-largest natural satellite in the Solar System, and the largest among planetary satellites relative to the size of the planet that it orbits (its primary).',
        'distance_from_earth': '384,400 km',
        'orbit_period': '27.3 days'
    }
}


@app.route('/')
def index():
    return render_template('index.html', planets=planets_info.keys())

@app.route('/planet/<string:planet_name>')
def get_planet_info(planet_name):
    planet = planets_info.get(planet_name.capitalize())
    return render_template('planet_info.html', planet_name=planet_name, planet=planet)

if __name__ == '__main__':
    app.run(debug=True)

