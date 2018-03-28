# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .utils import ExpiringTokenAuthentication
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from smog.models import User
from .serialization import UserDetailSerializers, UserRegisterSerializers
from rest_framework import status
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler


# from djang


class UserViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	queryset = User.objects.all()
	serializer_class = UserRegisterSerializers
	authentication_classes = (authentication.SessionAuthentication, JSONWebTokenAuthentication)



	def get_serializer_class(self):
		if self.action == "create":
			return UserRegisterSerializers
		elif self.action == 'retrieve':
			return UserDetailSerializers
		return UserDetailSerializers

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = self.perform_create(serializer)
		print(serializer.data)
		ret = serializer.data

		payload = jwt_payload_handler(user)
		ret['token'] = jwt_encode_handler(payload)
		ret['name'] = user.username
		# 加token
		# token_set = Token.objects.filter(user=user)
		# if token_set:
		# 	request.header['Authorization'] = token_set[0].key
		header = self.get_success_headers(serializer.data)
		return Response(ret, status=status.HTTP_201_CREATED, headers=header)

	def perform_create(self, serializer):
		print('hello')
		return serializer.save()

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)