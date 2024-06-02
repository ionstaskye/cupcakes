"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, jsonify
from models import db, connect_db, Cupcake
from datetime import datetime


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "Secretsecret"

connect_db(app)
with app.app_context():db.create_all()

@app.route("/")
def show_home():

    return render_template("base.html")

@app.route("/cupcakes")
def list_all_cupcakes():
    """Return JSON for cupcakes"""

    cupcakes = Cupcake.query.all()
    serialized = [Cupcake.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.route("/cupcakes/<cupcake_id>")
def list_specific_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = Cupcake.serialize(cupcake)

    return jsonify(cupcake = serialized)

@app.route("/cupcakes" methods = ["POST"])
def create_cupcake():

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    new_cupcake = Cupcake(flavor=flavor, size= size, rating = rating, image = image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = Cupcake.serialize(new_cupcake)

    return (jsonify(cupcake=serialized), 201)

@app.route("/cupcakes/<int:cupcake_id>" methods = ["PATCH"])
def edit_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json["flavor"]
    cupcake.size = request.json["size"]
    cupcake.rating = request.json["rating"]
    cupcake.image = request.json["image"]

    db.session.add(cupcake)
    db.session.commit()

    serialized = Cupcake.serialize(cupcake)

    return (jsonify(cupcake=serialized))

@app.route("/cupcakes/<int:cupcake_id>" methods = ["DELETE"])
def edit_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message = "DELETED!")