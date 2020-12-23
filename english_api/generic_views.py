from rest_framework import generics

from . import models
from . import serializers


class ListCreateWords(generics.ListCreateAPIView):
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializer
    
class RetriveUpdateDestroyWord(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializer