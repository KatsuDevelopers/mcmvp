from rest_framework import serializers
from .models import PinModel

class PinModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PinModel
        fields = ['pin_number']