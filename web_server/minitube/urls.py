from django.http import JsonResponse
from django.urls import path, include

urlpatterns = [
    path('ht', lambda x: JsonResponse({'status': 'ok'})),
    path('', include('minitube.apps.urls'))
]
