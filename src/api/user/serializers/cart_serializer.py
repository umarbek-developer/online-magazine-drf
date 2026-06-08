from rest_framework.serializers import ModelSerializer
from apps.order.models import Cart

class CartListSerializer(ModelSerializer):

    class Meta:
        model = Cart 
        fields = '__all__'


class CartCreateSerializer(ModelSerializer):

    class Meta:
        model = Cart 
        fields = '__all__'


class CartUpdateSerializer(ModelSerializer):

    class Meta:
        model = Cart 
        fields = '__all__'


class CartDestorySerializer(ModelSerializer):

    class Meta:
        model = Cart 
        fields = '__all__'
