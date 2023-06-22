
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CareerViewSet
router = DefaultRouter()
router.register('career', CareerViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
