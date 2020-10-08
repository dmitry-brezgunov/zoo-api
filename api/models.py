from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    possition = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('last_name', 'first_name', )


class AnimalPlace(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    specifications = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    additional_information = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class AnimalType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    preferable_food = models.TextField(blank=True)
    additional_information = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Animal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    animal_place = models.ForeignKey(
        AnimalPlace, on_delete=models.SET_NULL, null=True,
        related_name='animals')

    animal_type = models.ForeignKey(
        AnimalType, on_delete=models.SET_NULL, null=True,
        related_name='animals')

    employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True,
        related_name='animals')

    employee_assign_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
