import werkzeug.exceptions


class ResourceNotFoundException(werkzeug.exceptions.HTTPException):
    code = 404
