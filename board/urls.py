from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    path('delete/<int:document_id>', document_delete, name='document_delete'),
    path('update/<int:document_id>', document_update, name='document_update'),
    path('create/<current_category_slug>/', documentCreate, name='document_create'),
    path('doc/<document_slug>/', documentDetail, name='document_detail'),
    path('<category_slug>/', documentList, name='document_in_category'),
    path('', documentList, name='document'),
]