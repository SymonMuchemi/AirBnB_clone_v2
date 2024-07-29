#!/usr/bin/python3
"""Simple program script"""
from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """print greeting

    Returns:
        str: returned string
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_string(text):
    """Displays a special C string"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_route(text='is fun'):
    """python route

    Args:
        text (str): a string

    Returns:
        str: Python is @text
    """
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
