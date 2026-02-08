from django.urls import path
from .views import (
    CategoriesView,
    MenuItemsView,
    CartView,
    OrdersView,
    OrderItemsView
)

urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('menu-items/', MenuItemsView.as_view(), name='menu-items'),
    path('cart/', CartView.as_view(), name='cart'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('order-items/', OrderItemsView.as_view(), name='order-items'),
]
