from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import BookModel
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import permissions



# Create your views here.
@api_view(['GET'])
def bookList(request):
    booksObj = BookModel.objects.all()
    serializer = BookSerializer(booksObj, many = True)
    return Response(serializer.data) 

@api_view(['POST'])
def bookCreate(request):
    bookObj = BookModel.objects.all()
    serializer = BookSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)





    
