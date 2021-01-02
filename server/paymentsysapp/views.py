# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import viewsets, filters,permissions
from AppModel.serializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from collections import OrderedDict
from AppModel.models import *
from django.db.models import Avg, Count, Min, Sum
import hashlib,urllib,random,logging,requests,base64
import json,time,django_filters,xlrd,uuid
from rest_framework import status
import time, datetime
import requests,configparser
from AppModel.WXBizDataCrypt import WXBizDataCrypt 
from django.conf import settings
from django.db.models import Max 



logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)
handler = logging.FileHandler("paymentsysapp.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


conf_dir = settings.CONF_DIR
cf = configparser.ConfigParser()
cf.read(conf_dir)
logger.info("成功加载配置文件 %s " % (conf_dir))

# 内部方法用于将对象返回值转换成json串
# done
def _generate_json_from_models(response_list):
    return HttpResponse(json.dumps(response_list),
                        content_type='application/json',
                        )


# 内部方法用于返回json消息
# done
def _generate_json_message(flag, message):
    if flag:
        return HttpResponse("{\"error\":0,\"msg\":\""+message+"\"}",
                            content_type='application/json',
                            )
    else:
        return HttpResponse("{\"error\":1,\"msg\":\""+message+"\"}",
                            content_type='application/json',
                            )

# 缴费接口
def pay_all(request):
    if reques.POST:
        id_card_num = request.POST['id_card_num']
        payment_id_list = request.POST['payment_id_list']
        try:
            if id_card_num:
                paymentinfo_list = PaymentInfo.objects.filter(stu_id_card_num=id_card_num).filter(payment_status='0').filter(id__in =payment_id_list)
                return return _generate_json_message(True,"缴费成功")
        except:
            return _generate_json_message(False,"缴费失败")
        


# 用户登录
def user_login(request):
    if request.POST:
        id_card_num = request.POST['id_card_num']
        # tel_num = request.POST['tel_num']
        try:
            if id_card_num:
                student_info = StudentInfo.objects.get(stu_id_card=id_card_num)
            if student_info is not None:
                return _generate_json_message(True,"登录成功")
            else:
                return _generate_json_message(False,"登录失败")
        except:
            return _generate_json_message(False,"登录失败")


# 获取学生付款列表
def get_student_pay_list_info(request):
    if request.POST:
        id_card_num = request.POST['id_card_num']
        try:
            if id_card_num:
                stu_bill_list = PaymentInfo.objects.filter(stu_id_card_num=id_card_num).filter(payment_status='0') 
                stu_info = StudentInfo.objects.get(stu_id_card=id_card_num)
                list_response = []
                total_price = 0
                for stu_bill in stu_bill_list:
                    total_price = total_price + int(stu_bill.payment_amount)
                    dict_tmp = {}
                    dict_tmp.update(stu_bill.__dict__)
                    dict_tmp.pop("_state", None)
                    list_response.append(dict_tmp)
                a = {"name": stu_info.stu_name,
                     "class": stu_info.class_name,
                     "tel_num": stu_info.stu_phone_num ,
                     "pay_item_list": list_response,
                     "total_price": total_price}
                logger.info("返回值为 %s" % (a))
                # return HttpResponse("{\"name\":\""+stu_info.stu_name+"\",\"class\":\""+stu_info.class_name+"\",\"tel_num\":\""+stu_info.stu_phone_num +"\",\"pay_item_list\":\""+list_response+"\"}",
                return HttpResponse(json.dumps(a),content_type='application/json',)
                # return _generate_json_from_models(list_response)
        except:
            return _generate_json_message(False, "get student bill  false")