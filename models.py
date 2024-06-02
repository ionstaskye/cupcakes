"""Models for Cupcake app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf

db= SQLAlchemy()

default_image = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):

    __tablename__ = "cupcakes"

    id = db.Column (db.Integer,
                    primary_key = True,
                    autoincrement = True)
    flavor = db.Column(db.String,
                        nullable = False)
    size = db.Column(db.String,
                    nullable = False)
    rating = db.Column(db.Float,
                       nullable =False )
    image = db.Column(db.String,
                        nullable=False,
                        default= default_image)

    def serialize(self):
        """Serialize a cupcake SQLAlchemy obj to dictionary."""

        return {
        "id": self.id,
        "flavor": self.flavor,
        "size": self.size,
        "rating": self.rating,
        "image": self.image
        }

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
