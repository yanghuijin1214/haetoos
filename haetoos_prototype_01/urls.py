"""haetoos_prototype_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from web.views import WebList,WebDetail,WebCommentWrite
from python.views import PythonList,PythonDetail,CommentWrite

from . import settings

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('grappelli-docs/', include('grappelli.urls_docs')), # grappelli docs URLS
    path('admin/', admin.site.urls, name = 'admin'),
    path('',include('login.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('lecture/web/',WebList.as_view()),
    path('lecture/web/<int:pk>/',WebDetail.as_view()),
    path('lecture/web/write/',WebCommentWrite.as_view()),
    path('lecture/python/',PythonList.as_view()),
    path('lecture/python/write/',CommentWrite.as_view()),
    path('lecture/python/<int:pk>/',PythonDetail.as_view()),
]

#when DEBUG is true
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)