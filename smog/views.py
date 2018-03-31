# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework import mixins
from pathlib import Path
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .utils import IsOwner
from django_filters import rest_framework
from smog.models import User, Tag, Folder, Picture
from .serialization import UserDetailSerializers, UserRegisterSerializers, TagSerializers, FolderContentSerializers, \
	UserFolderSerializers,PictureSerializers
from rest_framework import status
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler, JSONWebTokenSerializer
from rest_framework import generics

# 检索 注册
class UserViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	queryset = User.objects.all()
	serializer_class = UserRegisterSerializers
	# JWT 验证
	authentication_classes = (authentication.SessionAuthentication, JSONWebTokenAuthentication)

	def get_serializer_class(self):
		if self.action == "create":
			return UserRegisterSerializers
		elif self.action == 'retrieve':
			return UserDetailSerializers
		return UserDetailSerializers

	def get_permissions(self):
		# 检索信息需要权限过
		if self.action == "retrieve":
			return [permissions.IsAuthenticated()]
		elif self.action == "create":
			return []
		return []

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = self.perform_create(serializer)
		print(serializer.data)
		ret = serializer.data
		# JWT:
		# 算法加密(base64(header) +.+ base64(payload) + salt)
		payload = jwt_payload_handler(user)
		ret['token'] = jwt_encode_handler(payload)
		ret['name'] = user.username

		header = self.get_success_headers(serializer.data)
		return Response(ret, status=status.HTTP_201_CREATED, headers=header)

	def perform_create(self, serializer):
		print('hello')
		return serializer.save()

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)


# class TageViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
# 	serializer_class = TagSerializers
# 	authentication_classes = (authentication.SessionAuthentication, JSONWebTokenAuthentication)
#
# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)


class UserFolderViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
	serializer_class = UserFolderSerializers
	queryset = Folder.objects.all()

	permission_classes = (IsAuthenticated,IsOwner)
	authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

	def get(self, request, *args, **kwargs):
		print('heer')
		return self.list(request, *args, **kwargs)

	def list(self, request, *args, **kwargs):
		userid = self.request.GET.get('user-id', None)
		if userid:
			try:
				userid = int(userid)
				queryset = Folder.objects.all().filter(creator=userid)
			except ValueError:
				queryset = Folder.objects.all().filter(creator__username=userid)
			print(',,', queryset)
			serializer = self.get_serializer(queryset, many=True)
			return Response(serializer.data)


# todo: 加权限
class FolderContentViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
	serializer_class = FolderContentSerializers

	ermission_classes = (IsAuthenticated, IsOwner)
	authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

	def get_queryset(self):
		return Folder.objects.filter(creator=1)

	def get(self, request, *args, **kwargs):
		print('folder congtent')
		return self.list(request, *args, **kwargs)

	def list(self, request, *args, **kwargs):
		folder_id = self.request.GET.get('folder-id', None)
		serializer = self.get_serializer_class()
		folder = self.get_queryset().filter(pk=folder_id)
		print('folder', folder[0].pictures)
		serializer = serializer(folder[0], context={'request': self.request})
		return Response(serializer.data, content_type='application/json')


class PictureListView(generics.ListAPIView):
	serializer_class = PictureSerializers
	filter_backends = (rest_framework.DjangoFilterBackend,)
	filter_fields = ('name', )
	def get_queryset(self):
		pass
def upload_pic(request):
	if request.method == "POST":
		from django.core.files.storage import DefaultStorage
		print(DefaultStorage().__class__)
		user = User.objects.get(pk=1)
		print(user.username)
		folder = Folder.objects.get(pk=2)
		pic = request.FILES.get('img', None)
		print(type(pic))
		print(Path.cwd())
		pg = Picture(uploader=user, folder=folder, content=pic)
		pg.save()
		print('nnnnnnn')
		# print(pg.content.path, pg.content.storage, pg.content.url)
		return render(request, 'indexx.html', {'message': 'success'})
	folder = Folder.objects.get(pk=2)
	pics = folder.picture_set.all()

	return render(request, 'indexx.html', {'pics': pics})
