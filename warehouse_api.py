from flask import Flask, jsonify

app = Flask(__name__)

inventory = {
    "SKU001": 42,
    "SKU002": 0,
    "SKU003": 17,
    "SKU004": 8,
    "SKU005": 103,
}


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
