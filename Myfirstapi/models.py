#!/usr/bin/env python3
from extensions import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    distance_from_sun = db.Column(db.String(100), nullable=True)
    orbit_period = db.Column(db.String(100), nullable=True)
