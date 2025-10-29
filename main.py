from flask import Flask, render_template, request, redirect, url_for
import os
from create_db import create_db
import hashlib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        password = hashlib.sha256(bytes(request.form["password"], "utf-8")).hexdigest()
        

        return redirect(url_for('index'))
    else:
        return render_template("index.html")


if __name__ == "__main__":
    db_in_dir = os.listdir()

    if "em.db" in db_in_dir:
        app.run()
    else:
        create_db()
        app.run()