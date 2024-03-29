"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('site_config/', admin.site.urls),
    path('', include('main.urls')),
    path('board/', include('board.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # Amazon AWS S3를 사용하지 않는 경우, media 파일 서빙하기
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]
