class Code():
    VALIDATION_FAILED = 1
    DOWNLOAD_FAILED = 2
    UPLOAD_FAILED = 3
    DELETE_FAILED = 4


class BadRequest(Exception):
    status_code = 400

    def __init__(self, code):
        Exception.__init__(self)
        self.code = code

    def to_dict(self):
        return {
            'code': self.code,
            'status': self.status_code,
        }