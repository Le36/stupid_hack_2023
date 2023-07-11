from flask import request, render_template

from app import app


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")


@app.route("/first", methods=["POST", "GET"])
def first():
    if request.method == "POST":
        if request.form["SubEmail"] == "google@google.com":
            return "done"
        return "first part of the puzzle"
