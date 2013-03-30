import uuid, os
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from mysamsung.models import Sale
from dao.employee_dao import EmployeeDAO
from mysamsung.dao.employee_dao import EmployeeDAO
from mysamsung.dao.customer_dao import CustomerDAO
from mysamsung.dao.supplier_dao import SupplierDAO


class LoginForm(forms.Form):
	user_name = forms.CharField(required=True,\
		label = _("login.user_name"),\
		widget = forms.TextInput(attrs={'class':'text'})\
		)
	password = forms.CharField(required=True,\
		label = _("login.password"),\
		widget=forms.PasswordInput(attrs={'class':'text'}))


class SaleForm(ModelForm):

	id = forms.CharField(required=False,initial=uuid.uuid1(),widget = forms.HiddenInput())
	supplier = forms.CharField(required=True,\
		label = _("sale.supplier"),\
		widget = forms.Select(attrs={'class':'text'})\
	)
	emp_id = forms.CharField(required=False,widget = forms.HiddenInput())
	new_supplier = forms.CharField(required=False,widget = forms.TextInput(attrs={'size':'16'}))
	model = forms.CharField(required=True,\
		label = _("sale.model"),\
		widget = forms.TextInput(attrs={'class':'text'})\
	)

	serial_number = forms.CharField(required=True,\
		label = _("sale.serial_number"),\
		widget = forms.TextInput(attrs={'class':'text'})\
	)

	new_employee= forms.CharField(required=False,widget = forms.TextInput(attrs={'size':'16'}))

	employee = forms.CharField(required=True,\
		label = _("sale.employee"),\
		widget = forms.Select(attrs={'class':'text'})\
	)

	purchase_date = forms.CharField(required=True,\
		label = _("sale.purchase_date"),\
		widget = forms.DateInput(attrs={'class':'text'})\
	)

	cost = forms.CharField(required=True,\
		label = _("sale.cost"),\
		widget = forms.TextInput(attrs={'class':'text'})\
	)

	new_customer = forms.CharField(required=False,widget = forms.TextInput(attrs={'size':'16'}))

	customer = forms.CharField(required=True,\
		label = _("sale.customer"),\
		widget = forms.Select(attrs={'class':'text'})\
	)

	sale_date = forms.CharField(required=True,\
		label = _("sale.sale_date"),\
		widget = forms.TextInput(attrs={'class':'text'})\
	)

	sale_price = forms.CharField(required=True,\
		label = _("sale.sale_price"),\
		widget = forms.TextInput(attrs={'class':'text'})\
	)

	ap_amount = forms.CharField(required=True,\
		label = _("sale.ap_amount"),\
		widget = forms.TextInput(attrs={'class':'text'})\
	)

	return_date = forms.CharField(required=True,\
		label = _("sale.return_date"),\
		widget = forms.TextInput(attrs={'class':'text'})\
	)

	gross_profit = forms.CharField(required=True,\
		label = _("sale.gross_profit"),\
		widget = forms.TextInput(attrs={'class':'text'})\
	)
	status = forms.CharField(required=True,\
		label = _("sale.status"),\
		widget = forms.Select(attrs={'class':'text'})\
	)

	comment = forms.CharField(required=True,\
		label = _("sale.comment"),\
		widget = forms.Textarea(attrs={'class':'text','rows':5,'cols':'94'})
	)

	def __init__(self, *args, **kwargs):
		super(SaleForm, self).__init__(*args,**kwargs)
		self.fields['id'] = forms.CharField(initial=uuid.uuid4(), widget=forms.HiddenInput())
		employeeDAO = EmployeeDAO()
		employees = employeeDAO.get_all()
		employee_list = []
		for employee in employees:
			tmp = []
			tmp.append(employee.name)
			tmp.append(employee.name)
			employee_list.append(tmp)
		self.fields['employee'] = forms.ChoiceField(choices=employee_list)
		self.fields['employee'].label = _("sale.employee") 


		supplierDAO = SupplierDAO()
		suppliers = supplierDAO.get_all()
		supplier_list = []
		for supplier in suppliers:
			tmp = []
			tmp.append(supplier.name)
			tmp.append(supplier.name)
			supplier_list.append(tmp)

		self.fields['supplier'] = forms.ChoiceField(choices=supplier_list)
		self.fields['supplier'].label = _("sale.supplier") 

		customerDAO = CustomerDAO()
		customers = customerDAO.get_all()
		customer_list = []
		for customer in customers:
			tmp = []
			tmp.append(customer.name)
			tmp.append(customer.name)
			customer_list.append(tmp)

		self.fields['customer'] = forms.ChoiceField(choices=supplier_list)
		self.fields['customer'].label = _("sale.customer") 

		not_settled = _('sale.status.not_settled')
		settled = _('sale.status.settled')
		status_list = [['0',not_settled],['1',settled]]
		self.fields['status'] = forms.ChoiceField(choices=status_list)
		self.fields['status'].label = _("sale.status") 

	class Meta:
		model = Sale
