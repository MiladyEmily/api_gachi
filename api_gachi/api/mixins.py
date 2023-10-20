from rest_framework import mixins, viewsets


class PostViewSet(
    mixins.CreateModelMixin,
    #mixins.ListModelMixin,
    #mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass
