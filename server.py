from flask import Flask, render_template
import util.network
import random
from datetime import datetime as dt
import api

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = dt.now().year
    return render_template("index.html", num=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    age = api.get_age(name)
    gender = api.get_gender(name)
    return render_template("guess.html", name=name.capitalize(), age=age, gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    # posts = [post for post in api.get_posts() if post["id"] == num]
    posts = api.get_posts()
    return render_template("blog.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True, host=util.network.get_ipaddress())
