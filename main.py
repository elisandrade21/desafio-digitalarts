from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/unique", methods=["POST"])
def unique():
    payload = request.json
    if len(payload["k"]) == payload["n"]:
        result = set(payload["k"])
        result = sorted(result)
        return jsonify({"result": result})
    else:
        return jsonify({"error": "The number of items in the list is not equal to the value entered."})


@app.route("/operation", methods=["POST"])
def operation():
    payload = request.json

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "%": lambda x, y: x % y
    }

    bin_num1 = f"0b{payload['number1']}"
    bin_num2 = f"0b{payload['number2']}"
    int_num1 = int(bin_num1, 2)
    int_num2 = int(bin_num2, 2)

    int_sum = operations[payload['operator']](int_num1, int_num2)
    bin_sum = bin(int_sum)[2:].zfill(8)

    return jsonify({"result": bin_sum})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
