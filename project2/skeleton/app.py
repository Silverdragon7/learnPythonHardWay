from flask import Flask
from flask import render_template
from flask import request
from bin.engine import *
from docs import *

app = Flask(__name__)


@app.route("/index", methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route("/start", methods=['POST', 'GET'])
def start():
    if request.method == "POST":
        choice = request.form['choice']
        return render_template("start.html", text=main(choice)) #funkcja tuuu
    else:
        return render_template("start.html", text="""Rok 1023 II ery
            Godzina 12.00
            Przechadzasz się ulicą tętniącego życiem miasteczka. Nagle ktoś mija cię z biegnąc w przeciwną stronę.
            Decydujesz się za nim podążyć?""")


if __name__ == "__main__":
    app.run()