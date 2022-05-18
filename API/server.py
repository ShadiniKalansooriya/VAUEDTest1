import logging

from flask import Flask
from flask import jsonify
from prometheus_flask_exporter import PrometheusMetrics

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")

api = Flask(__name__)
metrics = PrometheusMetrics(api)

metrics.info("app_info", "App Info, VAUED Assignment 2", version="1.0.0")


@api.route("/flask-prometheus-grafana-VAUED/")
def hello():
    return jsonify(say_hello())


def say_hello():
    return {"message": "This is our VAUED Assignment 2"}

@api.route("/semester1/")
def semester1():
    return jsonify(say_semester1())


def say_semester1():
    return {"message": "This is the page for semester1"}

@api.route("/semester2/")
def semester2():
    return jsonify(say_semester2())


def say_semester2():
    return {"message": "This is the page for semester2"}

@api.route("/semester3/")
def semester3():
    return jsonify(say_semester3())


def say_semester3():
    return {"message": "This is the page for semester3"}

@api.route("/semester4/")
def semester4():
    return jsonify(say_semester4())


def say_semester4():
    return {"message": "This is the page for semester4"}