from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "ok"


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


@app.route("/soma/<int:a>/<int:b>")
def soma_endpoint(a, b):
    return jsonify(resultado=soma(a, b)), 200


def soma(a, b):
    return a + b


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

