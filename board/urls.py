from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    # document 관련 경로
    path('', document_list, name='document'),
    path('<category_slug>/', document_list, name='document_in_category'),
    path('doc/<document_slug>/', document_detail, name='document_detail'),
    path('create/<current_category_slug>/', document_create, name='document_create'),
    path('update/<int:document_id>', document_update, name='document_update'),
    path('delete/<int:document_id>', document_delete, name='document_delete'),

    # comment 관련 경로
    path('comment/create/<int:document_id>', comment_create, name='comment_create'),
    path('comment/update/<int:comment_id>', comment_update, name='comment_update'),
    path('comment/delete/<int:comment_id>', comment_delete, name='comment_delete'),

    path('ajax/get_steam_app/', steam_app, name='get_steam_app'),
]