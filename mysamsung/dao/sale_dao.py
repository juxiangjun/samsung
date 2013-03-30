#!/usr/bin/env python 
#coding: utf-8

from mysamsung.models import Sale

class SaleDAO:

    def get_all(self):
        return Sale.objects.all();


    def query(self,start_date, end_date, employee, customer, supplier, status):
		result = None
		return result
