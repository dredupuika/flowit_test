from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:order_id>/', views.detail, name='detail'),
    path('<int:order_id>/pdf', views.pdf, name='pdf'),
    path('<int:order_id>/email_pdf', views.email_pdf, name='email_pdf'),
]
