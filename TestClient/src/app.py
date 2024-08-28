from flask import Flask

_blueprints = []
flask_app = Flask(__name__)


def add_blueprint(blueprint):
    _blueprints.append(blueprint)


def register_blueprints():
    for blueprint in _blueprints:
        flask_app.register_blueprint(blueprint)
