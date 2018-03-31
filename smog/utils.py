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
from rest_framework import permissions
from .models import User


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
		if timezone.now() > (token.created() + timedelta(5)):
			raise exceptions.AuthenticationFailed(_('Token had expired'))
		return (token.user, token)


class IsOwner(permissions.BasePermission):
	# REW:权限搞定
	def has_permission(self, request, view):
		u_id = request.GET.get('user-id')
		try:
			ud = int(u_id)
			us = User.objects.filter(pk=ud)
		except ValueError:
			us = User.objects.filter(username=u_id)
		u = us[0]
		return request.user == u
