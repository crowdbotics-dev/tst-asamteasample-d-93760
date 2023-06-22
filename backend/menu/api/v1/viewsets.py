from rest_framework import authentication
from menu.models import Career
from .serializers import CareerSerializer
from rest_framework import viewsets

class CareerViewSet(viewsets.ModelViewSet):
    serializer_class = CareerSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Career.objects.all()