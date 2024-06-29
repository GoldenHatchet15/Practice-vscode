#!/usr/bin/env python3

from db_setup import app, db, create_tables, Planet

def populate_planet_data():
    if not Planet.query.first():  # Check if the table is empty
        planets = [
            Planet(name='Mercury', description='Mercury is the closest planet to the Sun...', distance_from_sun='57.91 million km', orbit_period='88 days'),
            Planet(name='Venus', description='Venus is the second planet from the Sun...', distance_from_sun='108.2 million km', orbit_period='225 days'),
            Planet(name='Earth', description='Earth is our home planet...', distance_from_sun='149.6 million km', orbit_period='365.25 days'),
            Planet(name='Mars', description='Mars is the fourth planet from the Sun...', distance_from_sun='227.9 million km', orbit_period='687 days'),
            Planet(name='Jupiter', description='Jupiter is the largest planet in the Solar System...', distance_from_sun='778.5 million km', orbit_period='4333 days'),
            Planet(name='Saturn', description='Saturn is the sixth planet from the Sun...', distance_from_sun='1.434 billion km', orbit_period='10759 days'),
            Planet(name='Uranus', description='Uranus is the seventh planet from the Sun...', distance_from_sun='2.871 billion km', orbit_period='30688 days'),
            Planet(name='Neptune', description='Neptune is the eighth planet from the Sun...', distance_from_sun='4.495 billion km', orbit_period='60182 days'),
            Planet(name='Pluto', description='Pluto is a dwarf planet in the Kuiper belt...', distance_from_sun='5.906 billion km', orbit_period='90560 days'),
            Planet(name='Moon', description='The Moon is Earth\'s only permanent natural satellite...', distance_from_sun='384,400 km', orbit_period='27.3 days')
        ]
        db.session.bulk_save_objects(planets)
        db.session.commit()
        print("Database populated with initial planet data.")
    else:
        print("Database already contains data.")

def setup_database():
    with app.app_context():
        create_tables()
        populate_planet_data()

if __name__ == '__main__':
    print("Starting table creation and data population...")
    setup_database()
