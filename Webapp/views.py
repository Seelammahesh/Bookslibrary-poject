from logging import error
from django.contrib.auth.urls import *
from django.shortcuts import render,redirect
from django.template.defaulttags import url
from django.contrib.auth.forms import  UserCreationForm
from .serializers import *
from .models import *
from django.contrib import messages
from rest_framework.decorators import api_view
from  rest_framework.response import Response
from  rest_framework.views import exception_handler
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import authenticate,login,logout
from rest_framework.permissions import  IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_200_OK,HTTP_404_NOT_FOUND

from django.core.exceptions import *
# Create your views here.

def register(request):
    form=UserCreationForm
    if request.method=='POST':
        regform=UserCreationForm(request.POST)
        if regform.is_valid():
            regform.save()
            messages.success(request,("User hasbeen registered"))
    return render(request,"registration/register.html",{'form':form})



#  for login to admin via 127.0.0.1:accounts/login  use username:Mahesh,pass:~!@#$%^&M


@api_view(['GET'])
def get_view(request):
    try:
        book=BooksLibrary.objects.all() #quarey set
        serializer=BookSerializer(book,many=True) #serializing the data into json
        return Response(serializer.data)
    except  ModuleNotFoundError as e:
        return Response(str(e),status=404)

@api_view(['POST'])
def create_book(request):
    book=BooksLibrary.objects.all()
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        messages.success(request,("Book added Succesfully"))
        if serializer in BooksLibrary:
            return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_200_OK,)


@api_view(['PUT'])
def update_view(request,id):
    try:
        book=BooksLibrary.objects.get(id=id)
        serializer=BookSerializer(instance=book,data=request.data)
        if serializer.is_valid():
            serializer.save()
    except ValidationError:
        print(" Student id DoestExit")
    return Response("Student Updated Successfully")

@api_view(['DELETE'])
#deleting an item
def delete_view(request,id):
    try:
       student = BooksLibrary.objects.get(id=id)
       student.delete()
    except ValidationError:
        print("Student id DoesNotExists")
    return  Response("Book deleted successfully",student.id)

