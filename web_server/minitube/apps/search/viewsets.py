from rest_framework.decorators import action

from .helpers import search_vid_via_title
from ..commons.responses import response_200
from ..commons.viewsets import BaseApiViewSet


class SearchVideoViewSet(BaseApiViewSet):

    @action(methods=['GET'], detail=False, url_path='yt')
    def search_youtube_vid_via_title_view(self, request, *args, **kwargs):
        query = request.query_params.get('query') or ''
        if query:
            out = search_vid_via_title(query)
        else:
            out = []

        return response_200(out)
