from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.category_list, name='category_list'),

    path('produtos/', views.product_list, name='product_list'),
    path('produtos/novo/', views.product_create, name='product_create'),
    path('produtos/<int:product_id>/', views.product_detail, name='product_detail'),
    path('produtos/<int:product_id>/editar/', views.product_update, name='product_update'),
    path('produtos/<int:product_id>/excluir/', views.product_delete, name='product_delete'),
]