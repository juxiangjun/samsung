#!/usr/bin/env python 
#coding: utf-8

from mysamsung.models import User

class UserDAO:

    def get_all(self):
        return User.objects.all();

    def get_login_user(self, user_name, password):
		result = None
		users = User.objects.filter(user_name=user_name, password=password).all()
		if len(users)>0:
			result = users[0]
		return result	
