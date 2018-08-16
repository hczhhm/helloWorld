#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pymysql
from TestModel.models import userinformation

@csrf_exempt

def register(request):
    httpInfo = {}
    # response = {}
    if request.method == 'POST':
        userdic = json.loads(request.body)
        userN = userdic['userName']
        passW = userdic['passWord']
        try:
           response = userinformation.objects.get(userName=userN)
           # httpInfo = {'rel': False, 'message': '您已经注册过了', 'data': {}}
        except userinformation.DoesNotExist:
            sql = userinformation(userName=userN, passWord=passW)
            sql.save()
            httpInfo = {'rel': True, 'message': '注册成功', 'data': {'userName':userN,'passWord':passW}}
        else:
            httpInfo = {'rel': False, 'message': '您已经注册过了', 'data': {}}
    else:

        httpInfo = {'rel':False,'message':'请求方式错误','data':{}}


    return HttpResponse(json.dumps(httpInfo),content_type='application/json;charset=utf-8')


