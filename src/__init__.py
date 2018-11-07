import os

from flask import Flask

import config


app = Flask('BinaryAPI')

app.config.from_object(config)
app.secret_key = os.urandom(24)
