# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
import uuid
from django.db import models

class Customer(models.Model):
    id = models.CharField(max_length=108, primary_key=True)
    name = models.CharField(max_length=108, blank=True)
    class Meta:
        db_table = u'customer'
	def __init__(self):
		id = uuid.uuid1()

class Employee(models.Model):
    id = models.CharField(max_length=108, primary_key=True)
    name = models.CharField(max_length=192, blank=True)
    class Meta:
        db_table = u'employee'
	def __init__(self):
		id = uuid.uuid1()


class Sale(models.Model):
    id = models.CharField(max_length=108, primary_key=True)
    sale_date = models.DateField(null=True, blank=True)
    emp_id = models.CharField(max_length=192, blank=True)
    employee = models.CharField(max_length=192, blank=True)
    model = models.CharField(max_length=108, blank=True)
    cost = models.FloatField(null=True, blank=True)
    sale_price = models.FloatField(null=True, blank=True)
    serial_number = models.CharField(max_length=192, blank=True)
    customer = models.CharField(max_length=192, blank=True)
    supplier = models.CharField(max_length=192, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    ap_amount = models.FloatField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    gross_profit = models.FloatField(null=True, blank=True)
    comment = models.CharField(max_length=768, blank=True)
    status = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'sale'
	def __init__(self):
		self.id = uuid.uuid1()

class Supplier(models.Model):
    name = models.CharField(max_length=192, primary_key=True)
    id = models.CharField(max_length=108, blank=True)
    class Meta:
        db_table = u'supplier'
	def __init__(self):
		id = uuid.uuid1()


class User(models.Model):
    id = models.CharField(max_length=108, primary_key=True)
    user_name = models.CharField(max_length=108, blank=True)
    password = models.CharField(max_length=108, blank=True)
    class Meta:
        db_table = u'user'

