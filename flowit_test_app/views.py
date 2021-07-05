from .models import Order
from django.http import Http404
from django.shortcuts import render

def index(request):
    order_list = Order.objects.all()
    return render(request, 'orders/index.html', {'order_list': order_list,})

def detail(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        product_list = order.orderproduct_set.all()
    except Order.DoesNotExist:
        raise Http404("Order does not exist")
    return render(request, 'orders/detail.html', {'order': order,'product_list':product_list,})
