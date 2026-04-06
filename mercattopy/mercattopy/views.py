from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from catalog.models import Product, Category
from sales.models import Sale, SaleItem


@login_required
def dashboard(request):

    today = timezone.now().date()
    month = timezone.now().month
    year = timezone.now().year

    # KPIs
    total_products = Product.objects.count()
    total_categories = Category.objects.count()

    total_sales = Sale.objects.filter(status='completed').count()

    total_revenue = Sale.objects.filter(
        status='completed'
    ).aggregate(total=Sum('total'))['total'] or 0

    # Hoje
    sales_today = Sale.objects.filter(
        status='completed',
        date__date=today
    ).count()

    revenue_today = Sale.objects.filter(
        status='completed',
        date__date=today
    ).aggregate(total=Sum('total'))['total'] or 0

    # Mês
    sales_month = Sale.objects.filter(
        status='completed',
        date__month=month,
        date__year=year
    ).count()

    revenue_month = Sale.objects.filter(
        status='completed',
        date__month=month,
        date__year=year
    ).aggregate(total=Sum('total'))['total'] or 0

    # Últimas vendas
    latest_sales = Sale.objects.order_by('-date')[:5]

    # Top produtos
    top_products = (
        SaleItem.objects
        .values('product__name')
        .annotate(total_sold=Sum('quantity'))
        .order_by('-total_sold')[:5]
    )

    # Estoque baixo
    low_stock_products = Product.objects.filter(stock__lte=3)

    context = {
        'total_products': total_products,
        'total_categories': total_categories,
        'total_sales': total_sales,
        'total_revenue': total_revenue,

        'sales_today': sales_today,
        'revenue_today': revenue_today,

        'sales_month': sales_month,
        'revenue_month': revenue_month,

        'latest_sales': latest_sales,
        'top_products': top_products,
        'low_stock_products': low_stock_products,
    }

    return render(request, 'dashboard/dashboard.html', context)