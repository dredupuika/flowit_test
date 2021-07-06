from .models import Order
from django.http import Http404, FileResponse, HttpResponse
from django.shortcuts import render

from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string

from weasyprint import HTML

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

def pdf(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        product_list = order.orderproduct_set.all()
    except Order.DoesNotExist:
        raise Http404("Order does not exist")

    pdf_name = 'order_' + str(order.id) + '.pdf'

    html_string = render_to_string('orders/detail.html', {'order': order,'product_list':product_list,})
    pdf_file = HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf()

    http_response = HttpResponse(pdf_file, content_type='application/pdf')
    http_response['Content-Disposition'] = 'filename="' + pdf_name + '"'

    return http_response
