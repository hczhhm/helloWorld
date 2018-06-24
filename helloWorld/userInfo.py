#!/usr/bin/env python
#-*- coding:utf-8 -*-
#黄致
from django.shortcuts import render
from django.http import HttpResponse
import json
def index(request):
    return HttpResponse(u'这是菜鸟的第一个接口')
def userInfo(request):
    name = request.GET['name']
    phone = request.GET['phone']
    sex = request.GET['sex']
    userdata = {'name':name,'phone':phone,'sex':sex}
    data = {'info':userdata,'rel':True,'message':'成功'}
    return HttpResponse(json.dumps(data),content_type='application/json;charset=utf-8')