#!/usr/bin/python3
"""A simple Flask application that returns a greeting message.

This module defines a Flask application that responds to the root path (`/`)
with the message "Hello HBNB!".

The application can be run directly using `python app.py` and will listen
on port 5000 by default.
"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Returns a greeting message."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays “HBNB”"""
    return "HBNB"
@app.route('/c/<some_text>', strict_slashes=False)
def c_route(some_text):
    """Displays C with additional anonymous text"""
    return "C {}".format(some_text.replace('_', ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<some_text>', strict_slashes=False)
def python_route(some_text="is cool"):
    """Displays Python with some other text, if no text provided sets 'is cool'
    as the default text
    """
    return "Python {}".format(some_text.replace('_', ' '))

@app.route('/number/<int:some_integer>', strict_slashes=False)
def number_route(some_integer):
    """Displays only integer numbers"""
    if type(some_integer).__name__ == 'int':
        return "{} is a number".format(some_integer)

@app.route('/number_template/<int:some_integer>', strict_slashes=False)
def number_template(some_integer):
    """Display a HTML structure if the value provide is an integer"""
    if type(some_integer).__name__ == 'int':
        return render_template('5-number.html', n=some_integer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
