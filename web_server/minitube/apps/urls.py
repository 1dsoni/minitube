from django.urls import path, include

urlpatterns = [
    path('', include('minitube.apps.search.urls')),
    path('', include('minitube.apps.crawler.urls')),
]
