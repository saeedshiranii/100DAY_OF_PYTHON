from flask import Flask, render_template, request
import requests

ENDPOINT_POST_LINK = "https://api.npoint.io/54c8ac8084403dbccbca"
posts = requests.get(ENDPOINT_POST_LINK).json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int>:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login", methods=["Post"])
def get_usr_pss():

    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"




if __name__ == "__main__":
    app.run(debug=True)
