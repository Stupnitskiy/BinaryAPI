from flask import render_template, request, Blueprint

from src import app

from src.binary_app import serialize
from src.binary_app import spec

from src.lib.validate import wrap_validate 
from src.lib.services import dropbox

"""
TODO:
    1) Write unit tests.
    2) Write documentation and comments.
"""

binary_bp = Blueprint('binary_bp', __name__, url_prefix='/api/binary')

@binary_bp.route("/get", methods=['GET'])
def get_list():
    files = dropbox.list_folder()
    return serialize.get_list(files)


@binary_bp.route("/get/<string:key>", methods=['GET'])
@wrap_validate(spec.get())
def get(key):
    return dropbox.download(key)


@binary_bp.route("/put", methods=['PUT'])
@wrap_validate(spec.put())
def put():
    form = request.form

    key = form['key']
    data = form['data']

    encoded_data = str.encode(data)
    result = dropbox.upload(encoded_data, key)

    return serialize.put(result)


@binary_bp.route("/delete/<string:key>", methods=['DELETE'])
@wrap_validate(spec.delete())
def delete(key):
    file = dropbox.delete(key)
    return serialize.delete(file)