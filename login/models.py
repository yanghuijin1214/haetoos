from django.db import models
    
# Create your models here.
class User(models.Model):
    # 회원가입하기 위한 id,password와 학번, 이름을 database 에 저장할 수 있도록 해보자

    haetoos_id=models.CharField(max_length=64,verbose_name="아이디", blank=True)
    haetoos_ps=models.CharField(max_length=128,verbose_name="비밀번호")
    student_id=models.IntegerField(verbose_name="학번")
    name=models.CharField(max_length=64,verbose_name="이름")
    phone_number=models.IntegerField(default=0,verbose_name="전화번호",blank=True)
    # max_length 는 data의 최대 길이 지정.
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name="등록시간")
    # auto_now_add =true 로 설정하면 자동으로 시간이 저장된다.
    # 등록시간이 자동으로 저장되도록 설정!


    # data 가 admin page 에서 어떻게 보여질지 data 이름을 정하는 함수
    # https://neung0.tistory.com/51 참조
    def __str__(self):
        return self.name
        # data의 name을 리턴해줌.


    # database의 table명 지정하기
    class Meta:
        db_table = 'haetoos_user'
        verbose_name = "해투스 사용자"
        verbose_name_plural = "해투스 사용자"  # 복수형

