from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import LimitOffsetPagination

from .error_lib.handler import custom_exception_handler


class BaseApiViewSet(GenericViewSet):
    parser_classes = (JSONParser,)
    permission_classes = (AllowAny,)
    pagination_class = LimitOffsetPagination

    def perform_authentication(self, request):
        # dont need native django authentication
        return

    def get_exception_handler(self):
        """
        Returns the exception handler that this view uses.
        """
        return custom_exception_handler
