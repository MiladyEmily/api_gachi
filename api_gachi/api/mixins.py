from rest_framework import mixins, viewsets


class GetPostViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    pass

class GetViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass
