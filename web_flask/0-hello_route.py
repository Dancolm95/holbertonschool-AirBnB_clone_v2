#!/usr/bin/python3
""" Script start a flask application and defines a single route.
Routes:
      /: Displays 'Hello HBNB'
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """handle requests for the root route"""
    return "Hello HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
