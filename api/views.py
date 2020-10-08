from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .filters import AnimalFilters, AnimalPlaceFilters
from .models import Animal, AnimalPlace, AnimalType, Employee
from .serializers import (AnimalPlaceSerializer, AnimalSerializer,
                          AnimalTypeSerializer, EmployeeSerializer)


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = AnimalFilters
    ordering_fields = '__all__'


class AnimalPlaceViewSet(ModelViewSet):
    queryset = AnimalPlace.objects.all()
    serializer_class = AnimalPlaceSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = AnimalPlaceFilters
    ordering_fields = '__all__'


class AnimalTypeViewSet(ModelViewSet):
    queryset = AnimalType.objects.all()
    serializer_class = AnimalTypeSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    ordering_fields = '__all__'


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    ordering_fields = '__all__'
