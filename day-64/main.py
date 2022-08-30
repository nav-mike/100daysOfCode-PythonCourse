from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
Bootstrap(app)
db = SQLAlchemy(app)


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class NewMovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Add movie")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(100), nullable=False)


@app.route("/")
def home():
    return render_template(
        "index.html", movies=Movie.query.order_by(Movie.rating.desc())
    )


@app.route("/movie/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    movie = Movie.query.get_or_404(id)
    form = RateMovieForm()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/movie/<int:id>/delete", methods=["POST"])
def delete(id: int):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/movie/new", methods=["POST"])
def select():
    form = NewMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        response = requests.get(
            f"https://api.themoviedb.org/3/search/movie?api_key=api-key-here&language=en-US&query={title}&page=1&include_adult=false"
        )
        return render_template("select.html", movies=response.json()["results"])


@app.route("/add", methods=["GET"])
def new():
    form = NewMovieForm()
    return render_template("add.html", form=form)


@app.route("/add/<int:id>", methods=["POST"])
def create(id: int):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{id}?api_key=api-key-here"
    )
    movie = response.json()
    m = Movie(
        title=movie["title"],
        year=movie["release_date"][:4],
        description=movie["overview"],
        rating=0,
        review="",
        img_url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
    )
    db.session.add(m)
    db.session.commit()
    return redirect(
        url_for("edit", id=Movie.query.filter_by(title=movie["title"]).first().id)
    )


if __name__ == "__main__":
    app.run(debug=True)
