#!/usr/bin/env python
#-*- coding:utf-8 -*-
#黄致
from django.shortcuts import render
from django.views.decorators import  csrf

#接收post请求数据
def myFirstPost(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['content']
    return render(request,'myfPost.html',ctx)