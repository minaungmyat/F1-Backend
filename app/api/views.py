from django.shortcuts import render
from rest_framework import generics, filters
from drivers.models import Driver
from races.models import Race, RaceResult
from .serializers import DriverSerializer, RaceSerializer, RaceResultSerializer

class DriverListView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'code', 'team', 'nationality']
    ordering_fields = ['first_name', 'last_name', 'code']

class RaceListView(generics.ListAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'circuit']
    ordering_fields = ['year', 'round', 'date', 'name']

class RaceResultsListView(generics.ListAPIView):
    queryset = RaceResult.objects.select_related('driver', 'race').order_by('position')
    serializer_class = RaceResultSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['driver__first_name', 'driver__last_name', 'driver__code', 'race__name']
    ordering_fields = ['position', 'points', 'fastest_lap_time']