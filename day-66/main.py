import random
from threading import local
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def serialize(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random_cafe():
    cafe: Cafe = random.choice(Cafe.query.all())
    return jsonify(cafe.serialize())


@app.route("/cafes", methods=["GET"])
def cafes():
    return jsonify([cafe.serialize() for cafe in Cafe.query.all()])


@app.route("/search", methods=["GET"])
def search():
    location = request.args.get("location")
    if cafe := Cafe.query.filter_by(location=location).first():
        return jsonify(cafe.serialize())
    else:
        return jsonify({"error": "No cafe found"})


## HTTP POST - Create Record
@app.route("/cafes", methods=["POST"])
def create_cafe():
    name = request.json["name"]
    map_url = request.json["map_url"]
    img_url = request.json["img_url"]
    location = request.json["location"]
    seats = request.json["seats"]
    has_toilet = request.json["has_toilet"] == "true"
    has_wifi = request.json["has_wifi"] == "true"
    has_sockets = request.json["has_sockets"] == "true"
    can_take_calls = request.json["can_take_calls"] == "true"
    coffee_price = request.json["coffee_price"]

    cafe = Cafe(
        name=name,
        map_url=map_url,
        img_url=img_url,
        location=location,
        seats=seats,
        has_toilet=has_toilet,
        has_wifi=has_wifi,
        has_sockets=has_sockets,
        can_take_calls=can_take_calls,
        coffee_price=coffee_price,
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(cafe.serialize())


## HTTP PUT/PATCH - Update Record
@app.route("/cafes/<int:id>", methods=["PUT", "PATCH"])
def update_price(id: int):
    cafe = Cafe.query.get(id)
    if cafe is None:
        return jsonify({"error": "No cafe found"})
    cafe.coffee_price = request.json["coffee_price"]
    db.session.commit()
    return jsonify(cafe.serialize())


## HTTP DELETE - Delete Record
@app.route("/cafes/<int:id>", methods=["DELETE"])
def delete_cafe(id: int):
    cafe = Cafe.query.get(id)
    if cafe is None:
        return jsonify({"error": "No cafe found"})
    db.session.delete(cafe)
    db.session.commit()
    return jsonify({"success": "Cafe deleted"})


if __name__ == "__main__":
    app.run(debug=True)
