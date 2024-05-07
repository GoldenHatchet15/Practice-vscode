#!/usr/bin/env python3
import time
from flask import Flask, jsonify

app = Flask(__name__)

# Data about planets stored in a dictionary
planets_info = {
    'Mercury': {
        'description': 'Mercury is the closest planet to the Sun and due to its proximity, it is not easily seen except during twilight. For every two orbits of the Sun, Mercury completes three rotations about its axis and up until 1965 it was thought to rotate only once.',
        'distance_from_sun': '57.91 million km',
        'orbit_period': '88 days'
    },
    'Venus': {
        'description': 'Venus is the second planet from the Sun and is Earth’s closest planetary neighbor. It’s one of the brightest objects in the night sky, and is often called the morning star or the evening star.',
        'distance_from_sun': '108.2 million km',
        'orbit_period': '225 days'
    },
    # Add other planets as needed
}

@app.route('/planet/<string:planet_name>')
def get_planet_info(planet_name):
    planet = planets_info.get(planet_name.capitalize())
    if planet:
        return jsonify(planet)
    else:
        return jsonify({'error': 'Planet not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
