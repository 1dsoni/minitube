from ...constants import ClientAccessStatus
from ...models import Client
from ....commons.utils import get_random_key


def get_client(identifier: str, secret: str) -> Client:
    if identifier == 'anonymous':
        return Client(
            identifier=identifier,
            secret=identifier
        )

    return Client.objects.filter(identifier=identifier, secret=secret).last()


def create_client(name):
    return Client.objects.create(
        name=name,
        identifier=get_random_key(),
        secret=get_random_key(),
        status=ClientAccessStatus.ALLOWED
    )
