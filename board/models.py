from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from django.shortcuts import resolve_url
import datetime
import os

User = get_user_model()

class SteamApp(models.Model):
    # app id
    appid = models.PositiveIntegerField(unique=True, db_index=True)
    # 이름
    name = models.CharField(max_length=100, db_index=True)
    # 이미지 URL
    image = models.TextField(blank=True)
    # 할인율
    discount_per = models.PositiveIntegerField(default=0)
    # 할인되기 전 가격
    init_price = models.CharField(max_length=10, blank=True)
    # 할인된 가격이나 최종 가격
    final_price = models.CharField(max_length=10, blank=True)
    # 개발자
    developer = models.CharField(max_length=200, blank=True)
    # 배급사
    publisher = models.CharField(max_length=200, blank=True)
    # 장르
    genre = models.CharField(max_length=200, blank=True)
    # 출시 예정 유무
    coming_soon = models.BooleanField(default=False)
    # 출시 일자
    release_date = models.CharField(max_length=30, blank=True)
    # 지원되는 언어
    supported_languages = models.CharField(max_length=200, blank=True)


class Category(models.Model):
    # 카테고리 이름
    name = models.CharField(max_length=50)
    # 카테고리 슬러그
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True, db_index=True)
    # 상위 카테고리
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='sub_categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('board:document_in_category', self.slug)


class Document(models.Model):
    # 카테고리 참조
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='documents')
    # 유저 모델 참조
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    # 글 제목
    title = models.CharField(max_length=50)
    # 문서 슬러그
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True, db_index=True)
    # ckeditor
    text = RichTextUploadingField()
    # 조회 수
    hits = models.PositiveIntegerField(default=0)
    # 첨부 파일
    attachment = models.FileField(upload_to='attachment/%Y/%m/%d', blank=True)
    # 추천
    recommend = models.ManyToManyField(get_user_model(), blank=True, related_name='recommend_doc')
    # 문서 생성 일자
    create_date = models.DateTimeField(auto_now_add=True)
    # 문서 수정 일자
    update_date = models.DateTimeField(auto_now=True)

    # 스팀 앱 이름
    app_name = models.CharField(max_length=100, blank=True, null=True)
    # 스팀 앱 이미지
    app_image = models.TextField(blank=True, null=True)
    # 스팀 앱 가격
    app_price = models.CharField(max_length=20, blank=True, null=True)
    # 스팀 앱 링크
    app_link = models.CharField(max_length=100, blank=True, null=True)
    # 스팀 앱 출시 일자
    app_release_date = models.CharField(max_length=30, blank=True, null=True)

    # 문서 순서
    doc_sort = models.PositiveIntegerField(default=1)
    # 할인 종료 일자
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['doc_sort']

    def __str__(self):
        return self.title + ":" + self.create_date.strftime('%Y.%m.%d %H:%M')

    def filename(self):
        return os.path.basename(self.attachment.name)

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
    # 문서 참조
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='comments')
    # 유저 참조
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    # 댓글
    text = models.TextField()
    # 댓글 생성 일자
    create_date = models.DateTimeField(auto_now_add=True)
    # 댓글 수정 일자
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username

    def formatcreatedatetime(self):
        return self.create_date.strftime('%Y.%m.%d %H:%M')

    def formatupdatedatetime(self):
        return self.update_date.strftime('%Y.%m.%d %H:%M')
