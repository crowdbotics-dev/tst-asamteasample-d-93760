from rest_framework import serializers
from menu.models import Career

class CareerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Career
        fields = "__all__"