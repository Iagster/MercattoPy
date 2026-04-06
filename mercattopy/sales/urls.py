from django.urls import path
from . import views

urlpatterns = [
    path('vendas/', views.sales_home, name='sales_home'),
]