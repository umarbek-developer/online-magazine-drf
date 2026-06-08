from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from apps.order.models import Cart 
from api.user.serializers.cart_serializer import CartListSerializer, CartCreateSerializer, CartUpdateSerializer, CartDestorySerializer


class CartListApiView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer


class CartCreateApiView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer



class CartListApiView(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer


class CartListApiView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer
