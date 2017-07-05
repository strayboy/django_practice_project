#coding=utf-8
from django.db import models

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField()
    bcomment = models.IntegerField()
    bisDelete = models.BooleanField()
    class Meta():
        db_table='bookinfo'

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField()
    book = models.ForeignKey('BookInfo') # 引号有先后顺序

    def showname(self):
        return self.hname