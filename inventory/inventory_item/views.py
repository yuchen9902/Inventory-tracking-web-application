from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
# Create your views here.
def index(request):
    items = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    context = {
        'items' : items,
        'form' :form,
    }
    return render(request, 'dashboard/index.html', context)
def delete(request, key):
    item = Product.objects.get(id=key)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    context = {
        'item': item
    }
    return render(request, 'dashboard/delete.html')

def edit(request, key):
    item = Product.objects.get(id=key)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm(instance=item)
    context = {
        'form' : form
    }
    return render(request, 'dashboard/edit.html', context)
# def product(request):
#     items = Product.objects.all()
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#     else:
#         form = ProductForm()
#     context = {
#         'items' : items,
#         'form' :form,
#     }
#     return render(request, 'dashboard/product.html', context)
