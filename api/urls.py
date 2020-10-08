from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AnimalPlaceViewSet, AnimalTypeViewSet, AnimalViewSet,
                    EmployeeViewSet)

router = DefaultRouter()
router.register('places', AnimalPlaceViewSet)
router.register('types', AnimalTypeViewSet)
router.register('animals', AnimalViewSet)
router.register('employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
