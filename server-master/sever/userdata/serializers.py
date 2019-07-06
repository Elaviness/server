from rest_framework import serializers
from userdata.models import GeoData

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoData
        fields = '__all__'