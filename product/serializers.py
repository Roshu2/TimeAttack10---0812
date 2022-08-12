from rest_framework import serializers

from .models import Product, Subscribe


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "start_date", "is_active")
        
class SubscribeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subscribe
        fields = ("id", "user", "product", "purchase_date", "subscribe_start", "subscribe_end")