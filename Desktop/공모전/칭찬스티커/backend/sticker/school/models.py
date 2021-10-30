from django.db import models
from student.models import Student,Point
# Create your models here.

class Academy(models.Model):
    academy_id=models.CharField(max_length=16,primary_key=True,verbose_name="학원 아이디")
    password=models.CharField(max_length=64,verbose_name="비밀번호")
    academy_name=models.CharField(max_length=20)
    register_date=models.DateField(auto_now_add=True,verbose_name="등록 시간")


#학급
class Class(models.Model):
    academy=models.ForeignKey(Academy,on_delete=models.CASCADE)
    class_name=models.CharField(max_length=20) #classname




class Credit(models.Model):
    credit_name=models.CharField(max_length=32,verbose_name="칭찬 이름")
    detail=models.CharField(max_length=100,verbose_name="상세 내용")
    point=models.IntegerField(verbose_name="포인트")

    academy=models.ForeignKey(Academy,on_delete=models.CASCADE)
