from rest_framework import serializers

from gachi.models import Name, Gachi


class NameSerializer(serializers.ModelSerializer):
    gachies = serializers.SlugRelatedField(
        many=True,
        slug_field='gachi',
        queryset = Gachi.objects.all()
    )
    class Meta:
        model = Name
        fields = ('name', 'gachies', 'slug')
