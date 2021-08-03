from . import views
from django.urls import path 

app_name = 'store'

urlpatterns = [
    path('', views.list_products, name ='list_products'),
    path('products/<slug:slug>', views.product_detail, name='product_detail'),
    path('search/<slug:cat_slug>/', views.list_categories, name='category_list'),
]
