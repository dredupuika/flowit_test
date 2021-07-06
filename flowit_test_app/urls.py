from django.urls import path

from . import order_views
from . import product_views
from . import employee_views

urlpatterns = [
    path('orders/', order_views.index, name='orders_index'),
    path('orders/<int:order_id>/', order_views.detail, name='orders_detail'),
    path('orders/<int:order_id>/pdf', order_views.pdf, name='orders_pdf'),
    path('orders/<int:order_id>/email_pdf', order_views.email_pdf, name='orders_email_pdf'),

    path('products/', product_views.index, name='products_index'),
    path('products/<int:product_id>/', product_views.detail, name='products_detail'),
    path('products/<int:product_id>/update', product_views.update, name='products_update'),

    path('employees/', employee_views.index, name='employees_index'),
    path('employees/<int:employee_id>/', employee_views.detail, name='employees_detail'),
    path('employees/<int:employee_id>/update', employee_views.update, name='employees_update'),
]
