#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pymysql
from TestModel.models import userinformation

@csrf_exempt

def login(request):
    httpInfo = {}
    if request.method == 'POST':
        userDic = json.loads(request.body)
        userN = userDic['userName']
        passW = userDic['passWord']
        try:
           reson = userinformation.objects.get(userName=userN)
           # print(reson)
           if reson.passWord == passW:
               httpInfo = {'rel': True, 'message': '登陆成功', 'data': {}}
           else:
               httpInfo = {'rel': False, 'message': '密码错误', 'data': {}}

        except userinformation.DoesNotExist:
           httpInfo = {'rel': False, 'message': '该用户还未注册', 'data': {}}
    else:
        httpInfo = {'rel': False, 'message': '请求方式错误', 'data': {}}
    return HttpResponse(json.dumps(httpInfo),content_type='application/json;charset=utf-8')
