from rest_framework import serializers

from gachi.models import Name


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('name', 'gachies') 
