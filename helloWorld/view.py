#!/usr/bin/env python
#-*- coding:utf-8 -*-
# from django.http import HttpResponse
from  django.shortcuts import  render

# def hello(request):
#     return HttpResponse("Hello world!")

def hello(request):
    context = {}
    context['hello'] = 'What hello World!'
    context['name'] = 'test'
    return  render(request,'hello.html',context)
