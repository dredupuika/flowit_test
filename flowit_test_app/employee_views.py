from .models import Employee
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):

    employee_list = Employee.objects.all()

    return render(request, 'employees/index.html', {'employee_list': employee_list,})

def detail(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        raise Http404("Employee does not exist")
    return render(request, 'employees/detail.html', {'employee': employee})

def update(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        raise Http404("Employee does not exist")

    employee.name = request.POST['name']
    employee.email = request.POST['email']
    employee.save()

    return HttpResponseRedirect(reverse('employees_detail', args=(employee.id,)))
