from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
	return render(request, 'myapp/home.html')

def simple(request):
	#import pdb;pdb.set_trace()
	if request.method == 'POST':
		name = request.POST.get('name')
		principle=request.POST.get('principle')
		time = request.POST.get('time')
		rate = request.POST.get('rate')
	obj = Si(name=name, principle=principle, time=time, rate=rate)
	obj.save()
	return HttpResponse('successfully store the data into DB')


def employees(request):
	return render(request, 'myapp/employee.html')

def employee_save(request):
	if request.method == 'POST':
		emp_id = request.POST.get('emp_id')
		name = request.POST.get('name')
		company =  request.POST.get('company')
		location =  request.POST.get('location')
		salary = request.POST.get('salary')

	emp = Employee(emp_id=emp_id, name=name, company=company, location=location, salary=salary)
	emp.save()
	data = Employee.objects.all()
	return render(request, 'myapp/data.html', {'data':data})

def average(request):
	emp_new = list()
	emp = Employee.objects.all()
	for i in emp:
		if i.salary > 30000:
			emp_new.append(i)
	return HttpResponse(emp_new)