#!/usr/bin/env python 
#coding: utf-8

from mysamsung.models import Customer

class CustomerDAO:

    def get_all(self):
        return Customer.objects.all();
