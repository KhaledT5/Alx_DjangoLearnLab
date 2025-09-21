from rest_framework import generics
from rest_framework import viewsets
from api.models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    Provides list, create, retrieve, update, partial_update and destroy actions for Book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
