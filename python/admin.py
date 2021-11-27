from django.contrib import admin
from .models import Python,Python_comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PythonAdmin(SummernoteModelAdmin):
    list_display=('lec_name','register_date')
    summernote_fields='__all__'
admin.site.register(Python,PythonAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('content','comment','user','anony')
admin.site.register(Python_comment,CommentAdmin)