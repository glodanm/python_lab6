from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://gloda:glodanmax123@localhost/studentdb?auth_plugin=mysql_native_password"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Entertainment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    price = db.Column(db.Integer)
    height = db.Column(db.Integer)
    max_people = db.Column(db.Integer)

def __init__(self, name, age, price, height, max_people):
    self.name = name
    self.age = age
    self.price = price
    self.height = height
    self.max_people = max_people


class EntertainmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age', 'price', 'height', 'max_people')
    
entertainment_schema = EntertainmentSchema()
entertainments_schema = EntertainmentSchema(many=True)


@app.route('/entertainment', methods=['POST'])
def add_post():
    name = request.json['name']
    age = request.json['age']
    price = request.json['price']
    height = request.json['height']
    max_people = request.json['max_people']

    new_entertainment = Entertainment(name=name, age=age, price=price, height=height, max_people=max_people)
    db.session.add(new_entertainment)
    db.session.commit()

    return entertainment_schema.jsonify(new_entertainment)
    
@app.route('/entertainment', methods=['GET'])
def get_entertainments():
    all_entertainments = Entertainment.query.all()
    result = entertainments_schema.dump(all_entertainments)
    return jsonify(result)

@app.route('/entertainment/<id>', methods=['GET'])
def get_entertainment(id):
    entertainment = Entertainment.query.get(id)
    return entertainment_schema.jsonify(entertainment)

@app.route('/entertainment/<id>', methods=['PUT'])
def put_entertainment(id):
    entertainment = Entertainment.query.get(id)
    if entertainment == None:
        abort(404)

    entertainment.name = request.json['name']
    entertainment.age = request.json['age']
    entertainment.price = request.json['price']
    entertainment.height = request.json['height']
    entertainment.max_people = request.json['max_people']

    db.session.commit()
    return entertainment_schema.jsonify(entertainment)


@app.route('/entertainment/<id>', methods=['DELETE'])
def delete_entertainment(id):
    entertainment = Entertainment.query.get(id)
    if entertainment == None:
        abort(404)
    db.session.delete(entertainment)
    db.session.commit()
    return entertainment_schema.jsonify(entertainment)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)