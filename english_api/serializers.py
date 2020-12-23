from rest_framework import serializers
from .models import Word





class WordSerializer(serializers.ModelSerializer):
    """ it will serializes the model object """
    
    class Meta:
        model = Word
        fields= '__all__'