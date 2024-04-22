#!/usr/bin/python3
"""
start a Flask app with routes
"""

from flask import Flask, render_template
flask_app = Flask(__name__)
flask_app.url_map.strict_slashes = False


@flask_app.route('/')
def hello_route():
    """return text"""
    return "Hello HBNB!"


@flask_app.route('/hbnb')
def hbnb_text():
    """return text"""
    return "HBNB"


@flask_app.route('/c/<text>')
def cg_text(text):
    """return given text"""
    return "C {}".format(text.replace('_', ' '))


@flask_app.route('/python')
@flask_app.route('/python/<text>')
def py_text(text="is cool"):
    """return python text"""
    return 'Python {}'.format(text.replace('_', ' '))


@flask_app.route('/number/<int:n>')
def num(n):
    """returns given int"""
    return "{:d} is a number".format(n)


@flask_app.route('/number_template/<int:n>')
def html_int(n):
    """returns a HTML page if it is an int"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000)
