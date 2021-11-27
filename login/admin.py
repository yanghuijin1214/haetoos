from django.contrib import admin
#사용한 admin theme : https://github.com/sehmaschine/django-grappelli
from .models import User as User1
from django.contrib.auth.models import User,Group

# Register your models here.
class HaedalMemberAdmin(admin.ModelAdmin):
    fields = ['name','student_id','haetoos_id',]

admin.site.register(User1,HaedalMemberAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)