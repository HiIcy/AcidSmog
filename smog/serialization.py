# _*_ coding:utf-8 _*_
"""
__Author__    :  Icy
__Date__      :  2018/3/27
__File__      :  serialization.py
__Desc__      :
"""
from .models import User, Folder, Video, Tag, Subject, Picture
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


# todo:?


class UserRegisterSerializers(serializers.ModelSerializer):
	email = serializers.EmailField(help_text="注册邮箱", required=True, allow_blank=False)
	username = serializers.CharField(help_text='用户名', required=True, allow_blank=False, label="用户名",
	                                 validators=[UniqueValidator(User.objects.all(), message='用户已经存在')])
	password = serializers.CharField(
		style={"input_type": "password"}, required=True, write_only=True, label="密码", help_text='密码'
	)

	def validate_email(self, value):
		emailers = User.objects.filter(email=value)
		if len(emailers) > 1:
			raise serializers.ValidationError("邮箱已注册")
		return value

	def create(self, validated_data):
		return User.objects.create(**validated_data)

	class Meta:
		model = User
		fields = ('email', 'username', 'password')


class UserDetailSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"


class PictureSerializers(serializers.ModelSerializer):
	class Meta:
		model = Picture
		fields = "__all__"


class VideoSerializers(serializers.ModelSerializer):
	class Meta:
		model = Video
		fields = "__all__"


class FolderSerializers(serializers.ModelSerializer):
	pictures = PictureSerializers(many=True)

	class Meta:
		model = Folder
		fields = "__all__"


class TagSerializers(serializers.ModelSerializer):
	class Meta(object):
		model = Tag
		fields = ("id", "title")
