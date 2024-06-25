from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.create_order, name='order_create'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('list/', views.order_list, name='order_list'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
