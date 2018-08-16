#!/usr/bin/env python
#-*- coding:utf-8 -*-
#黄致
from django.shortcuts import render
from django.http import HttpResponse
import  json
from django.views.decorators.csrf import csrf_exempt
import pymysql

@csrf_exempt

def catMyInfo(request):
    data = {}
    if request.method == 'POST':
        dic = json.loads(request.body)
        # cursor = connection.cussor()
        # cursor.execute('select * from userTable where userId = %s',dic['userId'])
        # row = cursor.fetchone()
        #cursorclass = pymysql.cursors.DictCursor 设置数据返回类型为字典，默认为数据
        #db = pymysql.connect('127.0.0.1', 'root', 'huangczh109@', 'letterService',cursorclass = pymysql.cursors.DictCursor)
        # cursor = db.cursor()
        db = pymysql.connect('118.31.54.12', 'root', 'huangczh109HM@', 'appNetWork',
                             cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        sql = "select * from userinformation where userId = '%s'" % dic['userId']
        cursor.execute(sql)
        results = cursor.fetchall()

        if results:
            row = results[0]
            userName = row['userName']
            mobile = row['mobile']
            userdic = {'userName':userName,'mobile':mobile}
            data = {'info': userdic, 'rel': True, 'message': '成功'}
        else:
            data = {'info': {}, 'rel': False, 'message': '查询失败'}

    else:
        data = {'info': {}, 'rel': False, 'message': '接口方式错误'}

    db.close()

    return HttpResponse(json.dumps(data),content_type='application/json;charset=utf-8')