from flask import Flask, jsonify
import sys

app = Flask(__name__)
args = sys.argv[1:]


@app.route("/")
def home():
    return jsonify(args)


@app.route("/healthz")
def healthz():
    return "OK"


if __name__ == "__main__":
    print("args:", args)
    app.run(host="0.0.0.0", port=5000)
