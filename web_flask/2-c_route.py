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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
