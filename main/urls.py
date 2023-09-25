from django.urls import path
from .views import CategoryProducts, SubProducts, ProductDetail

app_name = 'main'
urlpatterns = [
    path('cat/<int:pk>/', CategoryProducts.as_view(), name = 'cat_prods'),
    path('subcat-prods/<int:pk>/', SubProducts.as_view(), name = 'subcat_prods'),
    path('product-detail/<int:pk>/',  ProductDetail.as_view(), name = 'product_detail'),
    
]
