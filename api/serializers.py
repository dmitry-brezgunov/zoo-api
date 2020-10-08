from rest_framework import serializers

from .models import Animal, AnimalPlace, AnimalType, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Employee


class AnimalSerializer(serializers.ModelSerializer):
    animal_place = serializers.SlugRelatedField(
        slug_field='name', queryset=AnimalPlace.objects.all())
    animal_type = serializers.SlugRelatedField(
        slug_field='name', queryset=AnimalType.objects.all())

    class Meta:
        fields = '__all__'
        model = Animal


class AnimalPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = AnimalPlace


class AnimalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = AnimalType
