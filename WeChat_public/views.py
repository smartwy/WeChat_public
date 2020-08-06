#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    WeChat_public
#F-Name:    views.py
#Login:     Administrator   
#Descripton:
#__Author__  Smartwy
#Date:      2020/6/17 15:27:14
#Version:

'''
    
'''

from django.http import HttpResponse
from django.shortcuts import render

def v_1(request):

	return render(request, "wyn.html")


