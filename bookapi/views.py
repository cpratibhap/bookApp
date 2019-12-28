from django.shortcuts import render
from .models import Book
from .serializers import BookSerialization
from rest_framework.viewsets import ModelViewSet


#GET GET/{id} POST PUT PATCH DELETE
class BookOperations(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerialization

