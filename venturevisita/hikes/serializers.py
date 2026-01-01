from rest_framework import serializers
from .models import Hike

class HikeSerializer(serializers.ModelSerializer):
    provider = serializers.ReadOnlyField(source='provider.username')
    
    class Meta:
        model = Hike
        fields = '__all__'

