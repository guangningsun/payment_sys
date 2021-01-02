# -*- coding:UTF-8 -*-
from django.contrib import admin
from AppModel.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin
import logging,json,datetime
from django.utils.html import format_html
from django import forms
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page
from django.utils.html import format_html,escape, mark_safe
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import time
import decimal


logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)
handler = logging.FileHandler("tjctwl.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)



# 学生管理
@admin.register(StudentInfo)
class StudentInfoAdmin(ImportExportModelAdmin):
    list_display = ['id','stu_num','stu_name','stu_id_card','stu_sexy','stu_phone_num','stu_desc','class_name']
    search_fields = ('stu_num','stu_name','stu_id_card','stu_sexy','stu_phone_num','stu_desc','class_name')
    fieldsets = [
       ('用户数据', {'fields': ['stu_num','stu_name','stu_id_card','stu_sexy','stu_phone_num','stu_desc','class_name'], 'classes': ['']}),
    ]
    list_per_page = 15


# 学生管理
@admin.register(ClassInfo)
class ClassInfoAdmin(ImportExportModelAdmin):
    list_display = ['class_id','class_num','class_name']
    search_fields = ('class_id','class_num','class_name')
    fieldsets = [
       ('用户数据', {'fields': ['class_id','class_num','class_name'], 'classes': ['']}),
    ]
    list_per_page = 15


# 缴费管理
@admin.register(PaymentInfo)
class PaymentInfoAdmin(ImportExportModelAdmin):
    list_display = ['payment_create_time','payment_class_name','payment_amount','payment_status','stu_num_id','stu_payment_time','payment_res_desc','merOrderId']
    search_fields = ('payment_create_time','payment_class_name','payment_amount','payment_status','stu_num_id','stu_payment_time','payment_res_desc','merOrderId')
    fieldsets = [
       ('用户数据', {'fields': ['payment_create_time','payment_class_name','payment_amount','payment_status','stu_num_id','stu_payment_time','payment_res_desc','merOrderId'], 'classes': ['']}),
    ]
    list_per_page = 15

#admin.site.register(CommodityCategory , MPTTModelAdmin)


admin.site.site_title = "缴费系统"
admin.site.site_header = "缴费系统1.0.1"


