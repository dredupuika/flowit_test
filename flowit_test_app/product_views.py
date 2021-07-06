from .models import Product
from django.http import Http404, FileResponse, HttpResponse
from django.shortcuts import render

def index(request):
    product_list = Product.objects.all()
    return render(request, 'products/index.html', {'product_list': product_list,})

def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'products/detail.html', {'product': product})
