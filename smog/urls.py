# _*_ coding:utf-8 _*_

from django.urls import path
from .views import upload_pic
app_name = 'smog'
urlpatterns = [
	path('picture',upload_pic,name='upload_pic'),
]