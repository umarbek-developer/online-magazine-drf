from rest_framework.serializers import ModelSerializer
from apps.order.models import Cart


class CartListSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'product', 'amount']
        read_only_fields = ['id']


class CartCreateSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product', 'amount']
        
    def validate_amount(self, value):
        if value < 1:
            raise ValueError('Amount must be at least 1')
        return value


class CartUpdateSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['amount']
        
    def validate_amount(self, value):
        if value < 1:
            raise ValueError('Amount must be at least 1')
        return value


class CartDestroySerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id']
        read_only_fields = ['id']



