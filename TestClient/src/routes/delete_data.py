from flask import Blueprint, Response
import app
import services.graphdb_service as graphdb_service


blueprint = Blueprint(__name__, __name__)
app.add_blueprint(blueprint)


@blueprint.route('/delete')
def delete_data():
    graphdb_service.delete_test_data()
    return Response('Data deleted!')
