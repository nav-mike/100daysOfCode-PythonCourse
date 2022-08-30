from flask import Flask
import random
app = Flask(__name__)


value = random.randint(0, 9)


def logger(function: callable):
    def wrapper(*args, **kwargs):
        print(f"{function.__name__} was called with args {args} and {kwargs}")
        result = function(*args, **kwargs)
        print(f"{function.__name__} returned '{result}'")
        return result

    wrapper.__name__ = function.__name__
    return wrapper


def bold(function: callable):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def italic(function: callable):
    def wrapper():
        return f"<i>{function()}</i>"
    return wrapper


def underline(function: callable):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route('/')
@logger
@bold
@italic
@underline
def hello_world() -> str:
    return 'Hello World!'


@app.route('/bye')
def bye() -> str:
    return 'Bye World!'


@app.route('/<name>/<user_id>')
@logger
def hello(name: str, user_id: int) -> str:
    return f"Hello {name} with {user_id}"


@app.route('/game')
def game() -> str:
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<br /><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"


@app.route('/game/<int:number>')
def guess(number: int) -> str:
    if number == value:
        return f"<h1>You found me!</h1>" \
               "<br /><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />"
    elif number > value:
        return f"<h1>Too high, try again!</h1>" \
               "<br /><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"
    else:
        return f"<h1>Too low, try again!</h1>" \
               "<br /><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />"


if __name__ == "__main__":
    app.run(debug=True)
