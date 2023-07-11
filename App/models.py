from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(150), nullable=False)

class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='crops')

class Field(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    location = db.Column(db.String(150))
    size = db.Column(db.Float)
    crop_id = db.Column(db.Integer, db.ForeignKey('crop.id'))
    crop = db.relationship('Crop', backref='fields')

class Harvest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_yield = db.Column(db.Float)
    date = db.Column(db.DateTime)
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'))
    field = db.relationship('Field', backref='harvests')