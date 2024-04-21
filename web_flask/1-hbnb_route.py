#!/usr/bin/python3
"""
starts a flask app
"""

from flask import Flask
flask_app = Flask(__name__)
flask_app.url_map.strict_slashes = False


@flask_app.route('/')
def hello_route():
    """returns text"""
    return "Hello HBNB!"


@flask_app.route('/hbnb')
def hbnb_text():
    """return text"""
    return "HBNB"


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000)
