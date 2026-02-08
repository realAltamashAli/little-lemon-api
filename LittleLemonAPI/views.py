from rest_framework import generics, permissions
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
    CartSerializer,
    OrderSerializer,
    OrderItemSerializer
)
from .permissions import IsManager, IsDeliveryCrew


# ======================
# CATEGORY APIs
# ======================
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated(), IsManager()]
        return [permissions.AllowAny()]


# ======================
# MENU ITEM APIs
# ======================
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated(), IsManager()]
        return [permissions.AllowAny()]


# ======================
# CART APIs (CUSTOMER ONLY)
# ======================
class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


# ======================
# ORDER APIs
# ======================
class OrdersView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name='Manager').exists():
            return Order.objects.all()

        if user.groups.filter(name='Delivery Crew').exists():
            return Order.objects.filter(delivery_crew=user)

        return Order.objects.filter(user=user)


# ======================
# ORDER ITEM APIs
# ======================
class OrderItemsView(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name='Manager').exists():
            return OrderItem.objects.all()

        if user.groups.filter(name='Delivery Crew').exists():
            return OrderItem.objects.filter(order__delivery_crew=user)

        return OrderItem.objects.filter(order__user=user)
