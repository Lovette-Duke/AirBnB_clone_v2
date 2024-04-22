#!/usr/bin/python3
"""
starts a flask app
"""

from flask import Flask, render_template
from models import *
from models import storage
flask_app = Flask(__name__)
flask_app.url_map.strict_slashes = False


@flask_app.route('/states')
def states():
    """returns HTML page of states"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states.html', states=states)


@flask_app.teardown_appcontext
def close_db(exception):
    """closes db"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

