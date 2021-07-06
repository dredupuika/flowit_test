from .models import Product
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):

    product_list = Product.objects.all()

    if request.GET:
        if request.GET['name']:
            product_list = product_list.filter(name=request.GET['name'])

        if request.GET['barcode']:
            product_list = product_list.filter(barcode=request.GET['barcode'])

        filter = {'name': request.GET['name'], 'barcode': request.GET['barcode'],}
    else:
        filter = {'name': '', 'barcode': '',}

    return render(request, 'products/index.html', {'product_list': product_list, 'filter': filter})

def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'products/detail.html', {'product': product})

def update(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    product.name = request.POST['name']
    product.barcode = request.POST['barcode']
    product.save()

    return HttpResponseRedirect(reverse('products_detail', args=(product.id,)))
