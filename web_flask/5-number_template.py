#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def cisnotfun(text):
    """Displays 'C' followed by <text>."""
    return f"C {format(text.replace('_', ' '))}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py(text='is cool'):
    """ display “Python ”, followed by the value of the text"""
    return f"Python {format(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    """display an HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
