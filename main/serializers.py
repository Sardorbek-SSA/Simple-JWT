from rest_framework import serializers
from .models import Toy

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ['id','name','color','price','created','owner']
        read_only_fields = ['owner']
        