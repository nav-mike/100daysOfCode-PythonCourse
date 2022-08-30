from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/')
def index():
    response = requests.get("https://api.npoint.io/9d5661a32d09209c23f8")
    response.raise_for_status()
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route('/<int:post_id>')
def post(post_id: int):
    response = requests.get("https://api.npoint.io/9d5661a32d09209c23f8")
    response.raise_for_status()
    posts = response.json()
    for post in posts:
        if int(post["id"]) == post_id:
            return render_template("post.html", post=post)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    is_sent = False
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        message = request.form.get("message")
        print(f"{name},\n{email},\n{phone_number},\n{message}")
        is_sent = True
    return render_template("contact.html", is_sent=is_sent)


if __name__ == "__main__":
    app.run(debug=True)
