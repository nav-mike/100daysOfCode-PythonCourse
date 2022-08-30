from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/9d5661a32d09209c23f8")
    response.raise_for_status()
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route('/<int:id>')
def show(id: int):
    response = requests.get("https://api.npoint.io/9d5661a32d09209c23f8")
    response.raise_for_status()
    posts = response.json()
    for post in posts:
        if int(post["id"]) == id:
            return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
