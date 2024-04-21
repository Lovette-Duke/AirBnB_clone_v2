#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
flask_app = Flask(__name__)


@flask_app.route('/', strict_slashes=False)
def hello_route():
    """returns text"""
    return "Hello HBNB!"


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000, debug=True)
