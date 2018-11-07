from flask import render_template, request, Blueprint

from src import app

from src.binary_app import serialize
from src.lib.services import dropbox

"""
TODO:
    1) Validation for input data.
    2) Download file from service.
    3) Standard all error responses from service.
    4) Write unit tests.
"""

binary_bp = Blueprint('binary_bp', __name__, url_prefix='/api/binary')

@binary_bp.route("/get", methods=['GET'])
def get_list():
    files = dropbox.list_folder()
    return serialize.get_list(files)


@binary_bp.route("/put", methods=['PUT'])
def put():
    form = request.form

    data = request.files.get('data')
    key = form.get('key')

    if not data or not key:
        return ('Invalid fields', 404)

    result = dropbox.upload(data.read(), key)
    return serialize.put(result)