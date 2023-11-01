from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

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


class GachiViewSet(GetPostViewSet):
    queryset = Gachi.objects.all()
    serializer_class = GachiSerializer

    def change_rate(self, naming, delta):
        """Базовая функция для изменения рейтинга гачи."""
        gachi = self.get_object()
        new_rate = {
            naming: getattr(gachi, naming) + 1,
            'rating': gachi.rating + delta,
        }
        serializer = GachiSerializer(gachi, data=new_rate, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    @action(
        ['post'],
        detail=True,
        permission_classes=(permissions.AllowAny,)
    )
    def like(self, request, *args, **kwargs):
        """Ставит лайк гаче."""
        return self.change_rate('likes', 1)
    
    @action(
        ['post'],
        detail=True,
        permission_classes=(permissions.AllowAny,)
    )
    def dislike(self, request, *args, **kwargs):
        """Ставит дизлайк гаче."""
        return self.change_rate('dislikes', -1)


class BaseNameViewSet(GetViewSet):
    queryset = BaseName.objects.all()
    serializer_class = BaseNameSerializer
