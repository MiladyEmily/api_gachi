from rest_framework import serializers

from gachi.models import Name, Gachi, BaseName
from gachi.helpers import gaching, translit_name


class NameGetSerializer(serializers.ModelSerializer):
    gachies = serializers.SlugRelatedField(
        many=True,
        slug_field='gachi',
        queryset = Gachi.objects.all()
    )
    class Meta:
        model = Name
        fields = ('name', 'gachies', 'slug')


class NamePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('name',)
    

    def to_representation(self, instance):
        """Заменяет сериализатор выдачи на NameGetSerializer."""
        ret = NameGetSerializer(
            instance,
            context={'request': self.context['request']}
        )
        return ret.data
    
        
    def create(self, validated_data):
        name = validated_data['name']

        if not Name.objects.filter(name=name).exists():
            slug = translit_name(name.lower())
            basename = BaseName.objects.create(
                basename=name,
                slug=slug,
            )
            name_obj = Name.objects.create(
                name=name,
                slug=slug,
                basename=basename
            )
            gachies = gaching(name)
            bulk_gachies = [
                Gachi(
                    gachi=gachi,
                    name = name_obj
                )
                for gachi in gachies
            ]
            Gachi.objects.bulk_create(bulk_gachies)
            return name_obj
        return Name.objects.filter(name=name)[0]
