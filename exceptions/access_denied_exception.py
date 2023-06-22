import werkzeug.exceptions


class AccessDeniedException(werkzeug.exceptions.HTTPException):
    code = 403
