from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions

from gachi.helpers import gaching, translit_name
from gachi.models import Name, Gachi, BaseName
from .serializers import NamePostSerializer
from .mixins import PostViewSet


class NameViewSet(PostViewSet):
    queryset = Name.objects.all()
    serializer_class = NamePostSerializer
    permission_classes = [permissions.AllowAny,]


# заменить на вьюсет
@api_view(['POST',])  # Применили декоратор и указали разрешённые методы
def gaching_name(request):
    name = request.data['name']
    status_code = status.HTTP_200_OK
    if not Name.objects.filter(name=name).exists():
        translit = translit_name(name.lower())
        basename = BaseName.objects.create(
            basename=name,
            slug=translit,
        )
        name_obj = Name.objects.create(
            name=name,
            slug=translit,
            basename=basename
            )
        gachies = gaching(name)
        # заменить на bulk_create
        for gachi in gachies:
            Gachi.objects.create(
                gachi=gachi,
                name = name_obj
            )
        status_code = status.HTTP_201_CREATED
    else:
        name_obj = Name.objects.filter(name=name)[0]
    serializer = NameGetSerializer(name_obj)
    return Response(serializer.data, status=status_code)
