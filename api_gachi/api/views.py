from rest_framework import permissions

from gachi.models import Name, Gachi, BaseName
from .serializers import NamePostSerializer, NameGetSerializer, GachiSerializer, BaseNameSerializer
from .mixins import GetPostViewSet, GetViewSet


class NameViewSet(GetPostViewSet):
    queryset = Name.objects.all()
    lookup_field = 'slug'
    serializer_class = NamePostSerializer
    permission_classes = [permissions.AllowAny,]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return NameGetSerializer
        return NamePostSerializer


class GachiViewSet(GetViewSet):
    queryset = Gachi.objects.all()
    serializer_class = GachiSerializer


class BaseNameViewSet(GetViewSet):
    queryset = BaseName.objects.all()
    serializer_class = BaseNameSerializer
