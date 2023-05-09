from django.shortcuts import render
from rest_framework import generics
from finance.models.library import Library
from finance.serializers import LibrarySerializer


class GetProductsLibraryRetrieve(generics.RetrieveAPIView):

    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    lookup_field = 'user'
