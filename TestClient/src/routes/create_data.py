from flask import Blueprint, Response
import app
import services.graphdb_service as graphdb_service


blueprint = Blueprint(__name__, __name__)
app.add_blueprint(blueprint)


@blueprint.route('/create')
def create_data():
    graphdb_service.create_test_data(10)
    return Response('Data created!')
