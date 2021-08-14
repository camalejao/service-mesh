import json
import uuid
from flask import Flask, make_response, request, jsonify
app = Flask(__name__)


@app.route("/customers")
def list_customers():
    customers = read_file()
    return jsonify(customers)


@app.route("/customers", methods = ["POST"])
def new_customer():

    customer = {
        "id": str(uuid.uuid4()),
        "firstName": request.json['firstName'],
        "lastName": request.json['lastName'],
        "street": request.json['street'],
        "city": request.json['city'],
        "state": request.json['state'],
        "zip": request.json['zip'],
        "country": request.json['country']
    }

    customers = read_file()
    customers.append(customer)
    write_file(customers)

    return make_response(jsonify({'customer': customer}), 201)


@app.route("/customers/<id>")
def get_customer(id):
    customers = read_file()
    
    for c in customers:
        if c['id'] == id:
            return jsonify(c)

    return make_response(jsonify({'error': 'not found'}), 404)


def read_file():
    with open("customers.json", "r") as f:
        data = json.load(f)
        return data


def write_file(data):
    with open("customers.json", "w") as f:
        data = json.dump(data, f)


if __name__ == "__main__":
    app.run()