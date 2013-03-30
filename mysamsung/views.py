# Create your views here.
import uuid, datetime
from django.utils.translation import ugettext as _
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import Q
from mysamsung.models import User
from mysamsung.models import Sale
from mysamsung.models import Employee
from mysamsung.models import Supplier
from mysamsung.models import Customer
from mysamsung.forms import LoginForm
from mysamsung.forms import SaleForm
from mysamsung.dao.user_dao import UserDAO
from mysamsung.dao.employee_dao import EmployeeDAO
from mysamsung.dao.customer_dao import CustomerDAO
from mysamsung.dao.supplier_dao import SupplierDAO
from mysamsung.dao.sale_dao import SaleDAO

def home(request):
	form = LoginForm()
	return render_to_response(\
			"index.html",\
			{'form':form},RequestContext(request))

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			dao = UserDAO()
			user = dao.get_login_user(form.cleaned_data['user_name'],form.cleaned_data['password'])
			if user == None:
				return render_to_response("index.html",{"form":form},RequestContext(request))
			else:
				request.session['user'] = user
				return show_main_page(request)
		else:
			return render_to_response("index.html",{"form":form},RequestContext(request))


def show_main_page(request):
	employeeDAO = EmployeeDAO()
	customerDAO = CustomerDAO()
	supplierDAO = SupplierDAO()
	saleDAO = SaleDAO()
	
	employeeList = employeeDAO.get_all()
	customerList = customerDAO.get_all()
	supplierList = supplierDAO.get_all()
	saleList = saleDAO.get_all()


	now = datetime.datetime.now()
	delta = datetime.timedelta(weeks=-4)
	last_month = now + delta 
	last_month = last_month.strftime('%Y-%m-%d')	
	today = now.strftime('%Y-%m-%d')
	

	return render_to_response('main.html',{"employeeList":employeeList,\
		"customerList":customerList,\
		"supplierList":supplierList,\
		"saleList": saleList,\
		"last_month": last_month,\
		"today": today\
		},RequestContext(request))


def show_edit_form(request):
	check_session(request)
	sale_id = request.POST['id'] 
	sale = None
	if sale_id != '-1':
		sale = Sale.objects.get(id=sale_id)
	form = None

	if sale != None:
		form = SaleForm(instance = sale)
	else:
		form = SaleForm()
	return render_to_response("sale_form.html",{'form':form},RequestContext(request))

def delete_sale_item(request):
	return check_session(request)
	sale_id = request.GET['id'] 
	sale = Sale.objects.get(id=sale_id)
	sale.delete()
	return show_main_page(request)

def save_sale_item(request):
	sale_id = request.POST['id'] 
	sale = None
	if sale_id != None:
		try:
			sale = Sale.objects.get(id=sale_id)
		except:
			print ''

	saleForm = None
	if sale != None:
		saleForm = SaleForm(request.POST, instance=sale)
	else:
		saleForm = SaleForm(request.POST)

	if saleForm.is_valid():	
		saleForm.save()
		return HttpResponse("success")
	else: 
		return render_to_response("errors.html",{'form':saleForm},RequestContext(request))

def do_query(request):
	start_date = request.POST['start_date']
	end_date = request.POST['end_date']
	employee = request.POST['qry_employee']
	customer = request.POST['qry_customer']
	supplier = request.POST['qry_supplier']
	status = request.POST['qry_status']
	query_set = []
	if len(start_date.strip())>1: 
		q = Q(sale_date__gt = start_date)
		query_set.append(q)

	if len(end_date.strip())>1:
		q = Q(sale_date__lt = end_date)
		query_set.append(q)

	if len(employee.strip())>1:
		q = Q(employee__exact = employee)
		query_set.append(q)

	if len(customer.strip())>1:
		q = Q(customer__exact = customer)
		query_set.append(q)

	if len(supplier.strip())>1:
		q = Q(supplier__exact = supplier)
		query_set.append(q)
	
	if len(status.strip())>0:
		q = Q(status__exact = status)
		query_set.append(q) 

	f = None 
	i = 0
	for q in query_set:
		if i==0:
			f = q
		else:
			f = f & q

		i = i+1
	saleList = None

	print f
	if f != None:
		saleList = Sale.objects.filter(f).order_by("sale_date").all()
	else:
		saleList = Sale.objects.all()

	return render_to_response('query_result.html',{"saleList": saleList},RequestContext(request))

	
def save_employee(request):
	employee = Employee()
	employee.id = uuid.uuid1()
	employee.name = request.POST['name']
	employee.save()
	return HttpResponse("success")

def save_supplier(request):
	supplier = Supplier()
	supplier.id = uuid.uuid1()
	supplier.name = request.POST['name']
	supplier.save()
	return HttpResponse("success")

def save_customer(request):
	customer = Customer()
	customer.id = uuid.uuid1()
	customer.name = request.POST['name']
	customer.save()
	return HttpResponse("success")

def check_session(request):
	if not request.session.get('user',False):
		return home(request) 
