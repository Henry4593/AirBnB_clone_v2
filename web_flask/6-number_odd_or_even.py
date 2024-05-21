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


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Returns a greeting message."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns the text 'HBNB'."""
    return "HBNB"
@app.route('/c/<some_text>', strict_slashes=False)
def c_route(some_text):
    """Accepts text in the URL, replaces underscores with spaces, and returns
    'C' followed by the modified text.
    """
    return "C {}".format(some_text.replace('_', ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<some_text>', strict_slashes=False)
def python_route(some_text="is cool"):
    """Accepts optional text in the URL, defaults to 'is cool' if no text
    provided.Replaces underscores with spaces and returns 'Python' followed by
    the modified text.
    """
    return "Python {}".format(some_text.replace('_', ' '))

@app.route('/number/<int:some_integer>', strict_slashes=False)
def number_route(some_integer):
    """Accepts an integer in the URL and returns a formatted string indicating
    the number."""
    if type(some_integer).__name__ == 'int':
        return "{} is a number".format(some_integer)

@app.route('/number_template/<int:some_integer>', strict_slashes=False)
def number_template(some_integer):
    """Accepts an integer in the URL and renders an HTML template displaying
    the number."""
    if type(some_integer).__name__ == 'int':
        return render_template('5-number.html', n=some_integer)

@app.route('/number_odd_or_even/<int:some_integer>', strict_slashes=False)
def number_odd_or_even(some_integer):
    """Accepts an integer in the URL, determines if it's even or odd,
    and renders an HTML template displaying the result."""
    if type(some_integer).__name__ == 'int':
        if some_integer % 2 == 0:
            text = "{} is even".format(some_integer)
            return render_template('6-number_odd_or_even.html', text=text)
        else:
            text = "{} is odd".format(some_integer)
            return render_template('6-number_odd_or_even.html', text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
