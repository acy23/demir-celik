from rest_framework import serializers 
from .models import Basic_metals
 
 
class Basic_metalSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Basic_metals
        fields = '__all__'
