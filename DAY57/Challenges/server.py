from flask import Flask, render_template
import requests
from detector import detector
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    year = datetime.datetime.now().year
    return render_template("index.html", year=year)


@app.route("/guess/<name>")
def guess_name(name):
    person = detector(name=name)
    return render_template("guess.html", name=name, age=person[1], gender=person[2])


@app.route("/blog")
def your_blog():
    test = requests.get("https://api.npoint.io/4ec070c5367cdf4d6818").json() # get respounse from my own made api for test using npoint.
    return render_template("blog.html", seri=test)


if __name__ == "__main__":
    app.run(debug=True)