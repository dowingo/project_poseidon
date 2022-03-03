import random

from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route("/") #wenn diese URL aufgerufen wird, soll etwas passieren
def hello():
    names = ["Domingo", "Furkan", "Gianni", "Lukas", "Syd", "Nemro", "Manu"]
    name_choice_ = random.choice(names)
    about_link = url_for("about")
    return render_template("index.html", name=name_choice_, link=about_link) #das wird dem Browser gesendet, wenn die URL aufgerufen wird


@app.route("/about")
def about():
    return "<h1>about test</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)

