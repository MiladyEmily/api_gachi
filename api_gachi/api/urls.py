from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NameViewSet, GachiViewSet, BaseNameViewSet


app_name = 'api'
router = DefaultRouter()
router.register('names', NameViewSet, basename='names')
router.register('gachies', GachiViewSet, basename='gachies')
router.register('basenames', BaseNameViewSet, basename='basenames')
urlpatterns = [
    path('gaching/', NameViewSet.as_view({'post': 'create'})),
    path('', include(router.urls)),
]
