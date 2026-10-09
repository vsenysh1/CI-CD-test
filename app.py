from flask import Flask, jsonify, render_template, request

from calc import add

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(status="ok", version=2, message="Hello from CI/CD!")


@app.get("/add")
def add_route():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return jsonify(result=add(a, b))
    

@app.get("/calculator")
def calculator():
    return render_template("calculator.html")