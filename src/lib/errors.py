from werkzeug.exceptions import HTTPException


class BadRequest(Exception):
    status_code = 400

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message

    def to_dict(self):
        response = {}

        response['status'] = self.status_code
        response['message'] = self.message

        return response