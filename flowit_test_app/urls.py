from django.urls import path

from . import order_views
from . import product_views

urlpatterns = [
    path('orders/', order_views.index, name='index'),
    path('orders/<int:order_id>/', order_views.detail, name='detail'),
    path('orders/<int:order_id>/pdf', order_views.pdf, name='pdf'),
    path('orders/<int:order_id>/email_pdf', order_views.email_pdf, name='email_pdf'),

    path('products/', product_views.index, name='index'),
    path('products/<int:product_id>/', product_views.detail, name='detail'),
]
