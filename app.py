import os
from flask import Flask, request, render_template, url_for, redirect, session
import psycopg2

app = Flask(__name__, static_folder='static')

#DATABASE_URL = os.environ.get("DATABASE_URL")

def connectdb():
    conn = psycopg2.connect(
    #instance ip address
    host="34.101.33.6",
    database="test-db",
    user="postgres",
    password="rMON}e7*I@Jo4B\-",
    port="5432")
    return conn

conn = connectdb()

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (" + 
            "user_id serial PRIMARY KEY," + 
            "username VARCHAR(50) NOT NULL, " + 
            "password VARCHAR(50) NOT NULL" + 
            ");")
conn.commit()
cur.close()
conn.close()

@app.route("/")
def index():
    return render_template("html/index.html")

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        redirect('/home')
    return render_template("html/login.html")

@app.route('/register',  methods=["GET","POST"])
def register():
    if request.method == "POST":
        # conn = connectdb()
        # cur = conn.cursor()
        # cur.execute("SELECT * FROM USERS")
        # rows = cur.fetchall()
        # for row in rows:
        #     print(row)
        # cur.close()
        # conn.close()
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        if password == confirm_password : 
            conn = connectdb()
            cur = conn.cursor()
            query = "INSERT INTO users values (%s,%s,%s)"
            data = (0,username,password)
            try:
                cur.execute(query,data)
                conn.commit()
            except (Exception, psycopg2.Error) as error:
                print(error)
            finally:
                if (conn):
                    cur.close()
                    conn.close()
                redirect('/home')
    return render_template("/html/register.html")

@app.route('/home')
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
