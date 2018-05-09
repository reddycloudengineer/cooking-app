from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters, generics
from .models import Place
from .serializers import PlaceSerializer, CategorySerializer
from .filters import PlaceFilter


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'category__name',)


class PlacesList(generics.ListAPIView):
    model = Place
    serializer_class = PlaceSerializer
    filter_class = PlaceFilter
    queryset = Place.objects.all()
