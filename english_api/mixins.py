from rest_framework import viewsets
from rest_framework import mixins

from . import models 
from . import serializers

class WordViewSet(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                mixins.UpdateModelMixin,
                viewsets.GenericViewSet):
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializer