import os
from flask import Flask, request, render_template, url_for
import psycopg2

app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template("html/home.html")

@app.route("/exchange/<currency>", methods=["GET","POST"])
def change(currency):
    if request.method == "POST":
        currency = request.form["currencys"]
        value = request.form["value"]
        if currency == "USD":
            total = int(value) * 16000
            return render_template("html/form.html", currency=currency, total = total)
        elif currency == "SGD":
            total = int(value) * 11417.81
            return render_template("html/form.html", currency=currency, total = total)
    return render_template("html/form.html", currency=currency, total = 0)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
