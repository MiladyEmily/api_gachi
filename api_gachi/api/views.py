from rest_framework import permissions

from gachi.models import Name
from .serializers import NamePostSerializer
from .mixins import PostViewSet


class NameViewSet(PostViewSet):
    queryset = Name.objects.all()
    serializer_class = NamePostSerializer
    permission_classes = [permissions.AllowAny,]
