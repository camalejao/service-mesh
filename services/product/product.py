import json
import uuid
from flask import Flask, make_response, request, jsonify
app = Flask(__name__)


@app.route("/products")
def list_products():
    products = read_file()
    return jsonify(products)


@app.route("/products", methods = ["POST"])
def new_product():

    product = {
        "id": str(uuid.uuid4()),
        "name": request.json['name'],
        "cost": request.json['cost']
    }

    products = read_file()
    products.append(product)
    write_file(products)

    return make_response(jsonify({'product': product}), 201)


@app.route("/products/<id>")
def get_product(id):
    products = read_file()
    
    for c in products:
        if c['id'] == id:
            return jsonify(c)

    return make_response(jsonify({'error': 'not found'}), 404)


def read_file():
    with open("products.json", "r") as f:
        data = json.load(f)
        return data


def write_file(data):
    with open("products.json", "w") as f:
        data = json.dump(data, f)


if __name__ == "__main__":
    app.run()