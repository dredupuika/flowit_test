from .models import Order, Employee
from django.http import Http404, FileResponse, HttpResponse
from django.shortcuts import render

from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string

from weasyprint import HTML

from django.core.mail import EmailMessage

def index(request):
    order_list = Order.objects.all()
    return render(request, 'orders/index.html', {'order_list': order_list,})

def detail(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        product_list = order.orderproduct_set.all()
    except Order.DoesNotExist:
        raise Http404("Order does not exist")

    if request.GET:
        if request.GET['name']:
            product_list = product_list.select_related('product').filter(product__name=request.GET['name'])

        if request.GET['barcode']:
            product_list = product_list.select_related('product').filter(product__barcode=request.GET['barcode'])

        filter = {'name': request.GET['name'], 'barcode': request.GET['barcode'],}
    else:
        filter = {'name': '', 'barcode': '',}

    return render(request, 'orders/detail.html', {'order': order,'product_list':product_list, 'filter':filter})

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

def email_pdf(request, order_id):
    try:
        # set a employee
        employee = Employee.objects.get(pk=1)
        order = Order.objects.get(pk=order_id)
        product_list = order.orderproduct_set.all()
    except Order.DoesNotExist:
        raise Http404("Order does not exist")

    pdf_name = 'order_' + str(order.id) + '.pdf'

    html_string = render_to_string('orders/detail.html', {'order': order,'product_list':product_list,})
    pdf_file = HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf()

    email = EmailMessage(
        'Order no: ' + str(order.id), 'Order attached.', 'from@example.com', [employee.email])
    email.attach(pdf_name, pdf_file, 'application/pdf')
    email.send()

    return render(request, 'orders/email_sent.html')
