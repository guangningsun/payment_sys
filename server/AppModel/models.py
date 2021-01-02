# -*- coding:UTF-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page
import datetime
from django.utils.html import format_html
from AppModel import *


# 学生类
class StudentInfo(models.Model):
    stu_num = models.CharField(max_length=200,verbose_name='学号')
    stu_name = models.CharField(max_length=200,verbose_name='学生姓名')
    stu_id_card = models.CharField(max_length=200,verbose_name='身份证号')
    stu_sexy = models.CharField(max_length=200,verbose_name='性别')
    stu_phone_num = models.CharField(max_length=200,verbose_name='手机号')
    stu_desc = models.CharField(max_length=200,verbose_name='备注')
    class_name = models.CharField(max_length=200,verbose_name='班级名称')
    # class_id = TreeForeignKey('ClassInfo',on_delete=models.CASCADE,null=True,blank=True,verbose_name='所在班级')
    
    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'
    
    def __str__(self):
        return self.stu_name

# 班级类
class ClassInfo(models.Model):
    class_id = models.CharField(max_length=200,verbose_name='班级id')
    class_num = models.CharField(max_length=200,verbose_name='班级号')
    class_name = models.CharField(max_length=200,verbose_name='班级名称')

    class Meta:
        verbose_name = '班级信息'
        verbose_name_plural = '班级信息'
    
    def __str__(self):
        return self.class_name


# 缴费信息类
class PaymentInfo(models.Model):
    payment_create_time = models.CharField(max_length=200)
    payment_class_name = models.CharField(max_length=200)
    payment_amount = models.CharField(max_length=200)
    payment_status = models.CharField(max_length=200)
    stu_num_id = models.CharField(max_length=200)
    stu_payment_time = models.CharField(max_length=200)
    payment_res_desc = models.CharField(max_length=200)
    merOrderId = models.CharField(max_length=200,default='None')

    class Meta:
        verbose_name = '缴费信息'
        verbose_name_plural = '缴费信息'
    