from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('category/<slug:slug>/', CategoryProductListView.as_view(), name='category_products'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]