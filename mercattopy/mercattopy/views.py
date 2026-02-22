from django.shortcuts import render
from catalog.models import Product, Category


def dashboard(request):
    context = {
        'total_products': Product.objects.count(),
        'total_categories': Category.objects.count(),
        'active_products': Product.objects.filter(is_active=True).count(),
        'inactive_products': Product.objects.filter(is_active=False).count(),
    }
    return render(request, 'dashboard/dashboard.html', context)