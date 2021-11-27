from django.contrib import admin
from .models import Web,Web_comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class WebAdmin(SummernoteModelAdmin):
    list_display=('lec_name','register_date')
    summernote_fields='__all__'
admin.site.register(Web,WebAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('content','comment','user','anony')
admin.site.register(Web_comment,CommentAdmin)