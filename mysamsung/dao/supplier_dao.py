#!/usr/bin/env python 
#coding: utf-8

from mysamsung.models import Supplier

class SupplierDAO:

    def get_all(self):
        return Supplier.objects.all();
