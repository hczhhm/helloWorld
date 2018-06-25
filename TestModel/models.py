from django.db import models

# Create your models here.
from django.db import models

class userinformation(models.Model):
        id = models.AutoField(max_length=11,db_column='UID',primary_key=True)
        userName = models.CharField(max_length=50,db_column='userName',blank=False)
        passWord = models.CharField(max_length=25,db_column='passWord',blank=False)
        mobile = models.CharField(max_length=11,db_column='mobile',blank=True)
        sex = models.CharField(max_length=10,db_column='sex',blank=True)
