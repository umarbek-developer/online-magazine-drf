from rest_framework.serializers import ModelSerializer
from apps.order.models import Order


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'total_price', 'address', 'status']
        read_only_fields = ['id', 'total_price', 'status']


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['address']
        
    def validate_address(self, value):
        if not value or len(value.strip()) < 5:
            raise ValueError('Address must be at least 5 characters')
        return value

