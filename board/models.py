from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from django.shortcuts import resolve_url
import datetime

"""
[Category]
name - 카테고리 이름
slug - 카테고리 슬러그
parent_category - 상위 카테고리

[Document]
category - 카테고리 참조
author - 유저 모델 참조
title - 글 제목
slug - 문서 슬러그
text - ckeditor로 구현
attachment - 첨부 파일
create_date - 생성 날짜
update_date - 수정 날짜
"""
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True, db_index=True)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='sub_categories')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('board:document_in_category', self.slug)

class Document(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='documents')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True, db_index=True)
    text = RichTextUploadingField()
    hits = models.PositiveIntegerField(default=0)
    attachment = models.FileField(upload_to='attachment/%Y/%m/%d', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    app_name = models.CharField(max_length=100, blank=True, null=True)
    app_image = models.TextField(blank=True, null=True)
    app_price = models.CharField(max_length=20, blank=True, null=True)
    app_link = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title + ":" + self.create_date.strftime('%Y.%m.%d %H:%M')

    def formatcreatedate(self):
        today_date = datetime.datetime.now().strftime('%m.%d')
        if today_date == self.create_date.strftime('%m.%d'):
            return self.create_date.strftime('%H:%M')
        else:
            return self.create_date.strftime('%m.%d')

    def formatcreatedatetime(self):
        return self.create_date.strftime('%Y.%m.%d %H:%M')

    def formatupdatedate(self):
        return self.update_date.strftime('%Y.%m.%d')

    def formatupdatedatetime(self):
        return self.update_date.strftime('%Y.%m.%d %H:%M')

    def get_absolute_url(self):
        return resolve_url('board:document_detail', self.slug)

class Comment(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username

    def formatcreatedatetime(self):
        return self.create_date.strftime('%Y.%m.%d %H:%M')

    def formatupdatedatetime(self):
        return self.update_date.strftime('%Y.%m.%d %H:%M')

