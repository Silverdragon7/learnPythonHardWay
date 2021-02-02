from flask import Flask
from flask import render_template
from flask import request
from bin.exs1 import # import funkcji zwracającej tekst

app = Flask(__name__)


@app.route("/index", methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route("/start", methods=['POST', 'GET'])
def start():
    # tu trzeba wrzucać teksty
    return render_template("start.html", text='testing')


if __name__ == "__main__":
    app.run()
