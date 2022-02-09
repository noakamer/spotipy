from flask import Flask, jsonify
import const

app = Flask(__name__)


@app.route("/hi", methods=["GET"])
def hello():
    return "hello world"


@app.route("/bye", methods=["GET"])
def bye():
    return "bye world"


@app.route("/artists", methods=["GET"])
def artists():
    return const.LIST_OF_ARTISTS

