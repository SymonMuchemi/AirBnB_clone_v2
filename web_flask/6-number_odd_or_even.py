#!/usr/bin/python3
"""Simple program script"""
from flask import Flask
from flask import url_for
from flask import render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_route(text='is cool'):
    """python route

    Args:
        text (str): a string

    Returns:
        str: Python is @text
    """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """number route

    Args:
        n (int): a number

    Returns:
        str: n is a number
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """display a HTML page only if n is an integer

    Args:
        n (number): the number

    Returns:
        html: template file
    """
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    num_str = f'{n} is '+ 'even' if n % 2 == 0 else f'{n} is odd'
    return render_template('6-number_odd_or_even.html', n=num_str)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
