import os

from flask import Flask, jsonify

import config

from src.lib.errors import BadRequest


app = Flask('BinaryAPI')

app.config.from_object(config)
app.secret_key = os.urandom(24)

# Register our blueprint for 'binary' endpoints
from src.binary_app.view import binary_bp
app.register_blueprint(binary_bp)


@app.errorhandler(BadRequest)
def badrequest_handler(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code

    return response