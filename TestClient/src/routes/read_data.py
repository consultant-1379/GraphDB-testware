from flask import Blueprint, Response
import app
import json
import services.read_service as read_service


blueprint = Blueprint(__name__, __name__)
app.add_blueprint(blueprint)


@blueprint.route('/read/start')
def start_reading():
    session_token = read_service.start_reading()
    result = {"token": session_token}
    result_as_json = json.dumps(result)
    response = Response(result_as_json, mimetype='application/json')
    return response


@blueprint.route('/read/stop/<token>')
def stop_reading(token):
    result = read_service.stop_reading(token)
    result_as_json = json.dumps(vars(result), default=(lambda obj: vars(obj)))
    response = Response(result_as_json, mimetype='application/json')
    return response
