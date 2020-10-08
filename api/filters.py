from datetime import timedelta

from django.db.models import Count
from django.utils import timezone
from django_filters import rest_framework as filters

from .models import Animal, AnimalPlace


class AnimalPlaceFilters(filters.FilterSet):
    two_animals = filters.BooleanFilter(method='filter_two_animals')

    def filter_two_animals(self, queryset, name, value):
        if value:
            return queryset.annotate(
                animal_count=Count('animals')
            ).filter(animal_count__gte=2)

        else:
            return queryset.annotate(
                animal_count=Count('animals')
            ).filter(animal_count__lt=2)

    class Meta:
        model = AnimalPlace
        fields = '__all__'


class AnimalFilters(filters.FilterSet):
    one_year_employee = filters.BooleanFilter(
        method='filter_one_year_employee')

    place_spec = filters.CharFilter(
        field_name='animal_place__specifications', lookup_expr='icontains')

    def filter_one_year_employee(self, queryset, name, value):
        time_threshold = timezone.now() - timedelta(days=365)
        if value:
            return queryset.filter(employee_assign_date__lt=time_threshold)
        else:
            return queryset.filter(employee_assign_date__gte=time_threshold)

    class Meta:
        model = Animal
        fields = '__all__'
