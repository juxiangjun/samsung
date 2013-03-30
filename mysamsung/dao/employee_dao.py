#!/usr/bin/env python 
#coding: utf-8

from mysamsung.models import Employee

class EmployeeDAO:

    def get_all(self):
        return Employee.objects.all();
