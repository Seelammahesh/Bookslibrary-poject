from .models import *
from  rest_framework import  serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=BooksLibrary
        fields= '__all__'