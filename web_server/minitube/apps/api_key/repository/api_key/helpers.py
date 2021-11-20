from ...models import ApiKey
from ....commons.utils import get_random_key


def save_api_key(name, key, key_config) -> ApiKey:
    return ApiKey.objects.create(
        name=name,
        key=key,
        identifier=get_random_key(),
        key_config=key_config,
        is_active=True
    )


def mark_key_inactive(name, identifier):
    return ApiKey.objects.filter(
        name=name,
        identifier=identifier,
        is_active=True
    ).update(is_active=False)


def fetch_new_active_key(name) -> ApiKey:
    return ApiKey.objects.filter(name=name, is_active=True).first()
