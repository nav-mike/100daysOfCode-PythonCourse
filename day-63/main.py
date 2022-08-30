from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from book_form import BookForm

app = Flask(__name__)
app.secret_key = 'some-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

all_books = []


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))
    rating = db.Column(db.Float)


db.create_all()


@app.route('/')
def home():
    return render_template('index.html', books=Book.query.all(),
                           books_length=Book.query.count())


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.name.data,
                    author=form.author.data, rating=form.rating.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
