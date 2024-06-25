from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('clothing/', views.ClothingListView.as_view(), name='clothing_list'),
    path('clothing/<int:pk>/', views.ClothingDetailView.as_view(), name='clothing_detail'),
    path('footwear/', views.FootwearListView.as_view(), name='footwear_list'),
    path('footwear/<int:pk>/', views.FootwearDetailView.as_view(), name='footwear_detail'),
    path('other/', views.OtherProductListView.as_view(), name='otherproduct_list'),
    path('other/<int:pk>/', views.OtherProductDetailView.as_view(), name='otherproduct_detail'),
    path('subcategory/<int:subcategory_id>/', views.ProductsBySubcategoryView.as_view(), name='products_by_subcategory'),
]
