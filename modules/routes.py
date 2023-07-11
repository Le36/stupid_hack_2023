from flask import request, render_template

from app import app


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
@app.errorhandler(Exception)
def error(error):
    return render_template("error.html")


@app.route("/first", methods=["POST", "GET"])
def first():
    if request.method == "POST":
        if request.form["SubEmail"] == "admin@hackjunction.com" and request.form["SubCountry"] == "Hack Me":
            return render_template("desktop.html")
        return render_template("index.html")


@app.route("/jigjijijkigdjkjkgnjdfnjgfdjnjn", methods=["POST", "GET"])
def winners():
    if request.method == "GET":
        return render_template("winners.html")


@app.route("/team", methods=["POST", "GET"])
def team():
    if request.method == "GET":
        return render_template("team.html")
