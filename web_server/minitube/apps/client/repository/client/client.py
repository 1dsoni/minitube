from .helpers import get_client
from ...constants import ClientAccessStatus
from ...exceptions import InvalidClientError
from ....client import error_codes


class ClientEntity(object):
    def __init__(self, token, secret):
        self.token = token
        self.name = ''
        self.validate(token, secret)

    def validate(self, token, secret):
        client = get_client(identifier=token, secret=secret)

        if client is None:
            raise InvalidClientError(error_codes.invalid_creds)
        if client.status == ClientAccessStatus.REVOKED:
            raise InvalidClientError(error_codes.access_revoked)

        self.name = client.name

    def record_success(self):
        pass

    def record_failure(self):
        pass
