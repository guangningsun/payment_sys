from rest_framework import serializers
from AppModel.models import *
from rest_framework.decorators import api_view


class StudentInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentInfo
        fields = ('stu_num','stu_name','stu_id_card','stu_sexy','stu_phone_num','stu_desc')


class ClassInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClassInfo
        fields = ('class_id','class_num','class_name')

class PaymentInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PaymentInfo
        fields = ('payment_create_time','payment_class_name','payment_amount','payment_status','stu_num_id','stu_payment_time','payment_res_desc','merOrderId')