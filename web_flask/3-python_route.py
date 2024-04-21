#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
