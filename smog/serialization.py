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
from . import _img_suffix


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
		# 加密
		return User.objects.create_user(**validated_data)

	class Meta:
		model = User
		fields = ('email', 'username', 'password')


class UserDetailSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"


class PictureSerializers(serializers.ModelSerializer):
	name = serializers.SerializerMethodField()
	type = serializers.SerializerMethodField()  # 方法序列化

	def get_name(self, obj):
		url = obj.content.url
		return url.rsplit('/')[-1]

	def get_type(self, obj):
		try:
			url = obj.content.url
			if url[-4:] in _img_suffix or url[-5:] in _img_suffix:
				return 'image'
		except Exception:
			return 'image'

	class Meta:
		model = Picture
		fields = "__all__"


class VideoSerializers(serializers.ModelSerializer):
	class Meta:
		model = Video
		fields = ("content", )


# TODO：用超链接的方式
class FolderContentSerializers(serializers.ModelSerializer):
	# user = serializers.HiddenField(default=serializers.CurrentUserDefault)
	# 只展示id
	# serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	pictures = PictureSerializers(many=True)
	# videos = VideoSerializers(many=True)

	class Meta:
		model = Folder
		# fields = ('id', 'name', 'create_time')
		fields = "__all__"


class UserFolderSerializers(serializers.ModelSerializer):
	# folders = FolderSerializers(many=True)
	# creator = serializers.HiddenField(def)

	class Meta:
		model = Folder
		fields = ('id', 'name', 'create_time')


class TagSerializers(serializers.ModelSerializer):
	class Meta(object):
		model = Tag
		fields = ("id", "title")
