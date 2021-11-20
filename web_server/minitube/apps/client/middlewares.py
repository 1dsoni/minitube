from django.utils.deprecation import MiddlewareMixin

from ..client.repository.client.client import ClientEntity


class ClientAuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # to allow free access to all, else remove <or 'anonymous'> to restrict
        token = request.headers.get('X-CLIENT-TOKEN') or 'anonymous'
        secret = request.headers.get('X-CLIENT-SECRET')
        client = ClientEntity(token, secret)
        setattr(request, 'client', client)
