#!/usr/bin/env python
#-*- coding:utf-8 -*-
#黄致

from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt  #解决post访问 403 错误
# 引用@csrf_protect
@csrf_exempt
def post_name(request):
    data = {}
    if request.method == 'POST':
       userID = ''
       dic = json.loads(request.body)
       if 'userId' in dic:
           userID = dic['userId']
       else:
           userID = ''

       if userID == '123':
          userInfo = {'name':'neo','phone':'10086','sex':'man'}
          data = {'info':userInfo,'rel':True,'message':'成功'}
       else:
          data = {'info':{},'rel':False,'message':'失败'}
    else:
        data = {'info': {}, 'rel': False, 'message': '该接口为post接口'}
    jsonstr = json.dumps(data)
    return HttpResponse(jsonstr,content_type='application/json;charset=utf-8')