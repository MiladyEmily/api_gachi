from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NameViewSet


app_name = 'api'
router = DefaultRouter()
router.register('names', NameViewSet, basename='names')
urlpatterns = [
    path('gaching/', NameViewSet.as_view({'post': 'create'})),
    path('', include(router.urls)),
    #path('names/', NameViewSet.as_view({'get': 'list', }))
]
