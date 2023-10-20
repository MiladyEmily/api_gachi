from django.urls import path

from .views import NameViewSet

urlpatterns = [
    path('gaching/', NameViewSet.as_view({'post': 'create'})),
]