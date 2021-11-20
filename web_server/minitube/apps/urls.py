from django.urls import path, include

urlpatterns = [
    path('', include('minitube.apps.search.urls'))
]
