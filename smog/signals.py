# _*_ coding:utf-8 _*_
"""
__Author__    :  Icy
__Date__      :  2018/3/27
__File__      :  signals.py
__Desc__      :
"""

from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from smog.models import User


@receiver(post_save,sender=User)
def create_auth_token(sender,instance=None,created=None,**kwargs):
	if created:
		Token.objects.create(user=instance)