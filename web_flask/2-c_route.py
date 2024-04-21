#!/usr/bin/python3
"""
starts a Flask app with routes
"""

from flask import Flask
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
    """returns given text"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000)
