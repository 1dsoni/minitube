from ...models import Trace
from ....commons.utils import get_random_key


def create_new_trace(entity,
                     entity_id,
                     request_status,
                     request_trace=None,
                     request_extra=None) -> Trace:
    return Trace.objects.create(
        entity=entity,
        entity_id=entity_id,
        request_trace=request_trace or get_random_key(),
        request_status=request_status,
        request_extra=request_extra
    )
