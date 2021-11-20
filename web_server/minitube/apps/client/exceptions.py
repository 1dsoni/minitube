from ..commons.error_lib.exceptions import BaseApiException


class InvalidClientError(BaseApiException):
    default_display_message = 'Failed to validate trace'
    status_code = 403
