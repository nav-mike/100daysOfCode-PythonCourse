import email
from typing import Callable
from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)
from forms import CommentForm, CreatePostForm, LoginForm, RegisterForm
from flask_gravatar import Gravatar
from functools import wraps

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
ckeditor = CKEditor(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)

##CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


##CONFIGURE TABLES


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="blog_posts")
    comments = relationship("Comment", back_populates="blog_post")


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    blog_posts = relationship("BlogPost")
    comments = relationship("Comment", back_populates="author")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="comments")
    blog_post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    blog_post = relationship("BlogPost", back_populates="comments")


db.create_all()


def admin_only(route: Callable):
    @wraps(route)
    def wrapper(*args, **kwargs):
        if current_user.email != "admin@email.com":
            return abort(403)
        return route(*args, **kwargs)

    return wrapper


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash("Email already exists", "danger")
            return redirect(url_for("login"))
        hashed_password = generate_password_hash(form.password.data, method="sha256")
        new_user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash("You have been successfully registered!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if user := User.query.filter_by(username=form.username.data).first():
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You have been successfully logged in!", "success")
                return redirect(url_for("get_all_posts"))
            else:
                flash("Invalid username or password", "danger")
                return redirect(url_for("login"))
        else:
            flash("Invalid username or password", "danger")
            return redirect(url_for("login"))
    return render_template("login.html", form=form)


@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("get_all_posts"))


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    form = CommentForm()
    return render_template("post.html", post=requested_post, form=form)


@login_required
@app.route("/post/<int:post_id>/comments", methods=["POST"])
def create_comment(post_id: int):
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(
            body=form.body.data, author_id=current_user.id, blog_post_id=post_id
        )
        db.session.add(new_comment)
        db.session.commit()
        flash("Your comment has been successfully added!", "success")
        return redirect(url_for("show_post", post_id=post_id))
    return redirect(url_for("show_post", post_id=post_id))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@login_required
@admin_only
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            date=date.today().strftime("%B %d, %Y"),
            author_id=current_user.id,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@login_required
@admin_only
@app.route("/edit-post/<int:post_id>")
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body,
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@login_required
@admin_only
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=9000)
