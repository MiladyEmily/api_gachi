from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from gachi.helpers import gaching, translit_name
from gachi.models import Name, Gachi, BaseName
from .serializers import NameSerializer

# заменить на вьюсет
@api_view(['POST',])  # Применили декоратор и указали разрешённые методы
def gaching_name(request):
    name = request.data['name']
    if not Name.objects.filter(name=name).exists():
        basename = BaseName.objects.create(
            basename=name,
            slug=translit_name(name),
        )
        name = Name.objects.create(
            name=name,
            slug=translit_name(name),
            basename=basename
            )
        gachies = gaching(name)
        # заменить на bulk_create
        for gachi in gachies:
            Gachi.objects.create(
                gachi=gachi,
                name = name
            )
    serializer = NameSerializer(data=request.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    #return Response({'name': name, 'gachi': gaching(name)})
