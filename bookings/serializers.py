from rest_framework import serializers
from .models import PricePackage

class PricePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricePackage
        fields = '__all__'
