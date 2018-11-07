import os

from flask import Flask

import config


app = Flask('BinaryAPI')

app.config.from_object(config)
app.secret_key = os.urandom(24)

# Register our blueprint for 'binary' endpoints
from src.binary_app.view import binary_bp
app.register_blueprint(binary_bp)