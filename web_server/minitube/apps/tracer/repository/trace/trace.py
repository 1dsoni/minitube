from .helpers import create_new_trace
from ...constants import TraceStatus


class TraceEntity(object):
    def __init__(self, entity, entity_id, extra=None):
        self.entity = entity
        self.entity_id = entity_id
        self.trace_id = create_new_trace(
            entity=self.entity,
            entity_id=self.entity_id,
            request_status=TraceStatus.CREATED,
            request_extra=extra
        ).request_trace

    def record_success(self):
        create_new_trace(entity=self.entity,
                         entity_id=self.entity_id,
                         request_status=TraceStatus.SUCCESS,
                         request_trace=self.trace_id)

    def record_failure(self):
        create_new_trace(entity=self.entity,
                         entity_id=self.entity_id,
                         request_status=TraceStatus.FAILED,
                         request_trace=self.trace_id)
