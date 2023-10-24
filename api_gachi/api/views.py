from rest_framework import permissions

from gachi.models import Name
from .serializers import NamePostSerializer, NameGetSerializer
from .mixins import GetPostViewSet


class NameViewSet(GetPostViewSet):
    queryset = Name.objects.all()
    lookup_field = 'slug'
    serializer_class = NamePostSerializer
    permission_classes = [permissions.AllowAny,]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return NameGetSerializer
        return NamePostSerializer
