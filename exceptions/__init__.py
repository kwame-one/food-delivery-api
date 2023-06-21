from pydantic import ValidationError

from exceptions.email_exists_exception import EmailExistException
from exceptions.exception_handler import resource_not_found_handler, bad_request_handler, email_exists_handler
from exceptions.not_found_exception import ResourceNotFoundException


def register_handlers(app):
    app.register_error_handler(ResourceNotFoundException, resource_not_found_handler)
    app.register_error_handler(ValidationError, bad_request_handler)
    app.register_error_handler(EmailExistException, email_exists_handler)
