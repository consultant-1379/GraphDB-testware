from flask import Blueprint, Response
import app


blueprint = Blueprint(__name__, __name__)
app.add_blueprint(blueprint)


@blueprint.route('/health')
def health_check():
    return Response('The test client is up and running!')
