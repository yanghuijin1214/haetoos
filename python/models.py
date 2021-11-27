from django.db import models

# Create your models here.
class Python(models.Model):
    lec_name=models.CharField(max_length=512,verbose_name="강의이름")
    lec_main=models.TextField(verbose_name="강의내용")
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name="등록날짜")
    # 댓글data. 다른 model과 연결

    def __str__(self):
        return self.lec_name
    
    class Meta:
        db_table='python_list'
        verbose_name="Python 강의"
        verbose_name_plural="Python 강의"

class Python_comment(models.Model):
    content=models.ForeignKey(Python,on_delete=models.CASCADE,verbose_name="강의제목")
    comment=models.TextField(verbose_name="댓글")
    user=models.CharField(max_length=64,verbose_name="이름")
    anony=models.CharField(max_length=8,verbose_name='익명',
        choices=(
            ('on','on'),
            ('off','off')
    ))
    dat=models.IntegerField(default=0)
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name="등록시간")