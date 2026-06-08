from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from apps.order.models import Cart 
from api.user.serializers.cart_serializer import CartListSerializer, CartCreateSerializer, CartUpdateSerializer, CartDestroySerializer


class CartListApiView(ListAPIView):
    serializer_class = CartListSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartCreateApiView(CreateAPIView):
    serializer_class = CartCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartUpdateApiView(UpdateAPIView):
    serializer_class = CartUpdateSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartDestroyApiView(DestroyAPIView):
    serializer_class = CartDestroySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
