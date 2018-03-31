# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from AcidSmog import settings


# Create your models here.
# class Role(models.Model):
# 	ADMINISTER =
class User(AbstractUser):
	USER_ROLE_CHOICES = (
		(0, "CommonUser"),
		(1, "SuperUser"),
		(2, "ADMINISTER")
	)
	avatar = models.ImageField(upload_to='upload/',blank=True, null=True)
	telephone = models.CharField(max_length=20, blank=True, null=True)
	about_me = models.CharField(max_length=50, null=True, blank=True)
	gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")), null=True, blank=True)
	role = models.IntegerField(default=0, choices=USER_ROLE_CHOICES)

	class Meta(object):
		verbose_name = "用户"
		unique_together = (('username', 'email'),)

	def __str__(self):
		return self.username


class Folder(models.Model):
	name = models.CharField(max_length=20)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	create_time = models.DateTimeField(auto_now_add=True)
	description = models.CharField(null=True, blank=True, max_length=50)

	class Meta(object):
		verbose_name = '画廊'

	def __str__(self):
		return '{user} 的 {folder}'.format(user=self.creator.username, folder=self.name)


# FIXME: 图片与文件夹是一对多还是多对多
class Picture(models.Model):
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.CharField(null=True, blank=True, max_length=40)
	timestamp = models.DateTimeField(auto_now_add=True)
	content = models.ImageField()
	folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="pictures")

	class Meta(object):
		verbose_name = "图片"

	def __str__(self):
		return '{user} 上传的 {picture}'.format(user=self.uploader.username, picture=self.content.name)


class Video(models.Model):
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.CharField(null=True, blank=True, max_length=40)
	timestamp = models.DateTimeField(auto_now_add=True)
	content = models.FileField()
	folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="videos")

	class Meta(object):
		verbose_name = '小视频'

	def __str__(self):
		return '{user} 上传的 {picture}'.format(user=self.uploader.username, picture=self.content.name)


class Subject(models.Model):
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.CharField(null=True, blank=True, max_length=40)
	timestamp = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=20)
	videos = models.ManyToManyField(Video)
	pictures = models.ManyToManyField(Picture)

	class Meta(object):
		verbose_name = '专题'

	def __str__(self):
		return '{0}'.format(self.title)


class Tag(models.Model):
	title = models.CharField(max_length=10)
	photos = models.ManyToManyField(Picture, related_name='tags', related_query_name='tag')

	class Meta(object):
		verbose_name = '标签'

	def __str__(self):
		return '{0}'.format(self.title)
