from django.utils.deprecation import MiddlewareMixin
import json
from .repository.trace.trace import TraceEntity


class TracerMiddleware(MiddlewareMixin):

    def process_request(self, request):
        client = getattr(request, 'client', None)
        request_meta = json.loads(
            json.dumps(request.META, default=str).encode('utf-8')
        )

        request_data = json.loads(
            json.dumps(request.POST, default=str).encode('utf-8')
        )

        request_path = json.loads(
            json.dumps(request.path, default=str).encode('utf-8')
        )

        if client is None:
            entity = 'anonymous'
            entity_id = 'anonymous'
        else:
            entity = client.name
            entity_id = client.token

        trace = TraceEntity(
            entity=entity,
            entity_id=entity_id,
            extra={
                'request_meta': request_meta,
                'request_data': request_data,
                'request_path': request_path
            }
        )

        setattr(request, 'trace', trace)

    def process_response(self, request, response):
        response['X-REQUEST-TRACE'] = request.trace.trace_id
        print(response)

        return response
