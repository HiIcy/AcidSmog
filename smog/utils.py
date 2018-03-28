# _*_ coding:utf-8 _*_
"""
__Author__    :  Icy
__Date__      :  2018/3/27
__File__      :  utils.py
__Desc__      :
"""
from rest_framework.authentication import TokenAuthentication
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions
from django.utils import timezone
from datetime import timedelta
from django.conf import settings


# 加入限期认证
class ExpiringTokenAuthentication(TokenAuthentication):
	def authenticate_credentials(self, key):
		model = self.get_model()
		try:
			token = model.objects.select_related('user').get(key=key)
		except model.DoesNotExist:
			raise exceptions.AuthenticationFailed(_('Invalid token'))
		if not token.user.is_active:
			raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
		if timezone.now() > (token.created()+timedelta(5)):
			raise exceptions.AuthenticationFailed(_('Token had expired'))
		return (token.user, token)
