

from rest_framework import serializers

from .models import StuInfo


class StuSerializers(serializers.ModelSerializer):
    
    class Meta:
    
        model = StuInfo
    
        fields = ['roll','Name', 'Address']
    
    
    