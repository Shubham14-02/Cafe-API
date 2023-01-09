from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint
from flask import jsonify

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

    def to_dict(self):
        dictionary = {}
        for col in self.__table__.columns:
            dictionary[col.name] = getattr(self, col.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def random():
    cafe = Cafe.query.filter_by(id=randint(1,6)).first()
    return jsonify(cafe=cafe.to_dict())


@app.route("/all")
def all():
    list_of_cafes = [cafe.to_dict() for cafe in db.session.query(Cafe).all()]
    return jsonify(cafe=list_of_cafes)


@app.route("/search")
def search():
    location = request.args.get("loc")
    cafe = Cafe.query.filter_by(location=location.capitalize()).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={
            "404: Not found": "Sorry, could not find cafe at that location"
         })


## HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add():
    cafe_response = request.form.to_dict()
    for key, value in cafe_response.items():
        if value == "True":
            cafe_response[key] = bool('True')
        elif value == "False":
            #if no values given to bool() it will return false
            cafe_response[key] = bool('')
            print(cafe_response[key])

    cafe = Cafe(**cafe_response)
    db.session.add(cafe)
    db.session.commit()
    success = {
        "success": "Successfully added new cafe"
    }
    return jsonify(
        response=success,
    )


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["GET", "PATCH"])
def update_price(cafe_id):
    price_to_update = Cafe.query.get(cafe_id)
    if price_to_update:
        new_price = request.args.get('new_price')
        price_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(
            Success="Successfully updated the price"
        )
    else:
        return jsonify(
            error={"not_found":"Sorry, cafe with that id is not to be found"}
        )


## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["GET", "DELETE"])
def report_closed(cafe_id):
    api_key = request.args.get('api_key')
    key = "ijwbcowbvouwyebrvouwbeocuhospkax"
    if api_key == key:
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(
                Success="Successfully deleted the cafe"
            )
        else:
            return jsonify(
                error={"not_found": "Sorry, cafe with that id is not to be found"}
            )
    else:
        return jsonify(
            error={"Authentication": "Access denied"}
        )


if __name__ == '__main__':
    app.run(debug=True)
