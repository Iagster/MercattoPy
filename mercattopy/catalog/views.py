from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Category, Product
from .forms import ProductForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'catalog/category_list.html', {
        'categories': categories
    })


def product_list(request):
    products = Product.objects.select_related('category').all()
    return render(request, 'catalog/product_list.html', {
        'products': products
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/product_detail.html', {
        'product': product
    })

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso.')
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'catalog/product_form.html', {
        'form': form,
        'title': 'Cadastrar Produto'
    })

def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso.')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'catalog/product_form.html', {
        'form': form,
        'title': 'Editar Produto'
    })

def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':

        if product.stock > 0:
            messages.error(
                request,
                'Não é possível excluir produto com estoque maior que zero.'
            )
            return redirect('product_list')

        product.delete()
        messages.success(request, 'Produto excluído com sucesso.')
        return redirect('product_list')

    return render(request, 'catalog/product_confirm_delete.html', {
        'product': product
    })
