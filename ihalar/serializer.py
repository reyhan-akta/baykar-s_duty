from rest_framework import serializers
from .models import IHA, Lessees, Orders

class IHASerializer(serializers.ModelSerializer):
    class Meta:
        model = IHA
        fields = ('id','brand','model','weight','category')

class LesseeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessees
        fields = ('id','username','email','password')

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id','user_id','order_id')