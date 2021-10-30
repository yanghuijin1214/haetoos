from django.db import models
from sticker.school.models import *
# Create your models here.


class Student(models.Model):
    school_choices=(
        ('사월','사월초등학교'),
        ('중산','중산초등학교'),
        ('매동','매동초등학교'),
        ('신매','신매초등학교'),
        ('욱수','욱수초등학교'),
        ('매호','매호초등학교'),
        ('시지','시지초등학교')
    )#영어로

    student_id=models.CharField(max_length=16,verbose_name="학생 아이디",primary_key=True)
    password=models.CharField(max_length=64,verbose_name="비밀번호")
    student_name=models.CharField(max_length=10,verbose_name="학생 이름")
    school=models.CharField(max_length=4,choices=school_choices,verbose_name="학교")
    academy=models.ForeignKey(Academy,on_delete=models.CASCADE)
    class_name=models.ForeignKey(Class,on_delete=models.CASCADE)
    total_point=models.IntegerField(verbose_name="총 포인트") 
    point=models.ForeignKey(Point,on_delete=models.CASCADE)
    register_date=models.DateField(auto_now_add=True,verbose_name="등록 시간")

    def __str__(self):
        return self.student_id

    class Meta:
        db_table = 'user'


class Point(models.Model):
    register_date=models.DateField(auto_now_add=True,verbose_name="포인트 등록 시간")
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    credit=models.ForeignKey(Credit,on_delete=models.CASCADE,verbose_name="칭찬 기준") 
    academy=models.ForeignKey(Academy,on_delete=models.CASCADE)
    #point?