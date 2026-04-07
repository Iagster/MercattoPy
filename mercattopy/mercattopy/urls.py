from django.contrib import admin
from django.urls import path, include
from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', dashboard, name='dashboard'),
    path('', include('catalog.urls')),
    path('', include('sales.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
]

handler403 = 'mercattopy.views.custom_403'