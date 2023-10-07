from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gachi.helpers import gaching


@api_view(['POST',])  # Применили декоратор и указали разрешённые методы
def gaching_name(request):
    name = request.data['name']
    return Response({'name': name, 'gachi': gaching(name)})