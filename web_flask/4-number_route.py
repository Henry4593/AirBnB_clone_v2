#!/usr/bin/python3
"""Flask app showcasing route handling and data processing.

This Flask application defines various routes demonstrating functionalities
for:
  - Handling basic text responses (`/`, `/hbnb`)
  - Accepting and processing URL variables (`/c/<some_text>`,
    `/python/<some_text>`)
  - Enforcing data types for URL variables (`/number/<int:some_integer>`)
  - Integrating with HTML templates for dynamic content (`/number_template`,
    `/number_odd_or_even`)

The application can be run using `python app.py` and listens on port 5000 by
default.
"""
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
