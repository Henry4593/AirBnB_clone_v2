#!/usr/bin/python3
"""A simple Flask application that returns a greeting message.

This module defines a Flask application that responds to the root path (`/`)
with the message "Hello HBNB!".

The application can be run directly using `python app.py` and will listen
on port 5000 by default.
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
