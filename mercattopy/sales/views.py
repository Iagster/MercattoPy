from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def sales_home(request):
    return render(request, 'sales/sales_home.html')