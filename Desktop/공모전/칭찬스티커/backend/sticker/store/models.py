from django.db import models
from student.models import Student

# Create your models here.
class Store(models.Model):
    store_id=models.CharField(max_length=16,primary_key=True,verbose_name="상점 아이디")
    password=models.CharField(max_length=64,verbose_name="비밀번호")
    store_name=models.CharField(max_length=20,verbose_name="상점 이름")

class Product(models.Model):
    store=models.ForeignKey(Store,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=20,verbose_name="상품명")
    point=models.IntegerField(verbose_name="포인트")


class Payment(models.Model):
    store=models.ForeignKey(Store,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    #승인여부: 승인되기전, 승인완료, 승인거부,환불
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    