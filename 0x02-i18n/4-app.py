#!/usr/bin/env python3
""" Python Module """
from flask_babel import Babel
from flask import Flask, render_template


class Config(object):
    """ Class for Babel """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Get locale parameters"""
    locale = request.args.get('locale')
    match = app.config['LANGUAGES']
    if locale and locale in match:
        return locale
    return request.accept_languages.best_match(match)


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """ Basic Template for Babel Implementation"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
