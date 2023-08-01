#!/usr/bin/env python3
"""basic flask babel app"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class with configuration for babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


@babel.localeselector
def get_locale():
    """checks language in supported languages lib"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_world():
    """ renders page when / is called """
    return render_template('1-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
