from rest_framework.views import APIView

from rest_framework.response import Response # IMPORT THIS BCZ WE WANT TO USE A NICE INTERFACE to render in multiple format
from rest_framework import status

from .models import Word 
from .serializers import WordSerializer


class WordList(APIView):
    """view to list all words in database """

    def get(self, request): # self because we create a function in the class self give us access to the attribute 
        # and method request because the user are going to nreguest the data
        words =  Word.objects.all()# access all the words instances and store it in the variable
        
        data = WordSerializer(words, many=True).data# many to True we want to serializer many items
        # dot data attribute is unrender serialise data of the response and we store all of this in variable called data
        return Response(data)
    
    def post (self, request):
        serializer = WordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

