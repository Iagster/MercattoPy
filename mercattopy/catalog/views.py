from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Category, Product
from .forms import ProductForm
from .decorators import admin_required


@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'catalog/category_list.html', {
        'categories': categories
    })


@login_required
def product_list(request):
    products = Product.objects.all()

    is_admin = request.user.groups.filter(name='Admin').exists()

    return render(request, 'catalog/product_list.html', {
        'products': products,
        'is_admin': is_admin
    })


@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/product_detail.html', {
        'product': product
    })


@login_required
@admin_required
def product_create(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso!')
            return redirect('product_list')

    else:
        form = ProductForm()

    return render(request, 'catalog/product_form.html', {
        'form': form
    })


@login_required
@admin_required
def product_update(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('product_list')

    else:
        form = ProductForm(instance=product)

    return render(request, 'catalog/product_form.html', {
        'form': form
    })


@login_required
@admin_required
def product_delete(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method != 'POST':
        return render(request, 'catalog/product_confirm_delete.html', {
            'product': product
        })

    if product.stock > 0:
        messages.error(request, 'Não é possível excluir produto com estoque maior que zero.')
        return redirect('product_list')

    product.delete()
    messages.success(request, 'Produto excluído com sucesso!')
    return redirect('product_list')