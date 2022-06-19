from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import json
import json
import random



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

@app.route('/formular', methods=["GET", "POST"])
def form():
    if request.method == "POST":
        data = request.form
        einkauf = data["einkauf"]
        datum = data["datum"]
        preis = data["preis"]
        kat = data["kat"]

        try:
            with open("data.json", "r") as open_file:
                inhalt = json.load(open_file)
        except FileNotFoundError:
            inhalt = []

        dict = {"Einkauf": einkauf, "Datum": datum, "Kategorie": kat, "Preis CHF": preis}
        inhalt.append(dict)

        with open("data.json", "w") as open_file:
            json.dump(inhalt, open_file, indent=4)
        return render_template("index.html")
    else:
        render_template("index.html")

@app.route("/ausgabenprotokoll")
def protokoll():
    with open("data.json", encoding="utf-8") as open_file:
        inhalt = json.load(open_file)
        return render_template("ausgabenprotokoll.html", inhalt=inhalt)

@app.route("/statistik")
def statistik():
    with open("data.json", encoding="utf-8") as open_file:
        ausgaben = json.load(open_file)
        count = len(ausgaben)
    about_link = url_for("statistik")
    summe = 0
    for el in ausgaben:
        summe += int(float(el["Preis CHF"]))

    with open("data.json") as open_file:
        ausgaben2 = json.load(open_file)
        dict_1 = {}
        for element in ausgaben2:
            for key, value in element.items():
                if key == "Kategorie":
                    dict_1.setdefault(value, []) #setdefault wird dazu verwendet um mehrere values einem Key zuzuordnen
                    dict_1[value].append(float(element["Preis CHF"]))

    for key, value in dict_1.items():
        value = sum(value)
        dict_1[key] = value


    highest_kat = max(dict_1, key=dict_1.get)

    return render_template("statistik.html", link=about_link, count=count, total_ausgaben=summe, highest_kat=highest_kat)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
