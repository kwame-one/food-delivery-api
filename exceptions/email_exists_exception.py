import werkzeug.exceptions


class EmailExistException(werkzeug.exceptions.HTTPException):
    code = 400
