from rest_framework import viewsets
from Books import models
from Books.api import serializers

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()