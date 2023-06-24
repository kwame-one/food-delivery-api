import werkzeug.exceptions


class OrderUpdateException(werkzeug.exceptions.HTTPException):
    code = 400
