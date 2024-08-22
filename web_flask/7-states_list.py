#!/usr/bin/python3
"""Simple program script"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def remove_sql_session(exception):
    """removes the current SQLAlchemy session
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    # states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    states = storage.all(State)
    return render_template('7-states_list.html', states=states, n=len(states))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
