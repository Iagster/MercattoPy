from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.category_list, name='category_list'),
    path('produtos/', views.product_list, name='product_list'),
    path('produtos/<int:product_id>/', views.product_detail, name='product_detail'),
]