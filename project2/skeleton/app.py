from flask import Flask
from flask import render_template
from flask import request
from bin.test import funkcja

app = Flask(__name__)


@app.route("/index", methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route("/start", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        choice = request.form['choice']
        return render_template("start.html", text=funkcja(choice)) #funkcja tuuu
    else:
        return render_template("start.html", text="tekst początkowy")

if __name__ == "__main__":
    app.run()
