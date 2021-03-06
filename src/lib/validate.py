import collections
from functools import wraps

from flask import request

from src.lib import update_dicts
from src.lib.errors import BadRequest, Code


def wrap_validate(schema):

    def _wrap_validate(f):

        @wraps(f)
        def wrapped(*args, **kwargs):
            if is_valid(schema, args, kwargs):
                return f(*args, **kwargs)

            raise BadRequest(Code.VALIDATION_FAILED)

        return wrapped

    return _wrap_validate


def is_valid(dict_scheme, args, kwargs):
    form = update_dicts(
        args, kwargs,
        request.args,
        request.form,
        request.json,
    )

    if not isinstance(dict_scheme, dict):
        return False

    for field in dict_scheme:
        data = form.get(field)

        for validator in dict_scheme[field]:
            if not validator(data):
                return False

    return True


def required(field):
    return field != None
