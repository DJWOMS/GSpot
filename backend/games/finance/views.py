from rest_framework import generics
from finance.models import Library, Offer
from finance.serializers import OfferSerializer, LibrarySerializer


class OfferAPIView(generics.CreateAPIView):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class ShowLibraryView(generics.RetrieveAPIView):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    lookup_field = 'user'
