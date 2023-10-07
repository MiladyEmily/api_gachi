from django.urls import path

from .views import gaching_name

urlpatterns = [
    path('gaching/', gaching_name),
]