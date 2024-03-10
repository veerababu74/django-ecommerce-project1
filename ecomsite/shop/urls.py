from django.urls import path
from shop.views import index,detail,checkout
app_name="shop"
urlpatterns = [
    path('', index, name='shop_index'),
     path('<int:id>/', detail, name='productdetails'),
     path('checkout/', checkout, name='productscheckout'),
    
]
