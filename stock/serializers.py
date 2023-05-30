from rest_framework import serializers
from .models import Kospi

class KospiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kospi
        fields = ['id', 'name', 'price', 'total_price']
        
