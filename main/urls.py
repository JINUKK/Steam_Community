from django.urls import path

from .views import rank_list

app_name = 'main'

urlpatterns = [
    path('', rank_list, name = 'ranklist'),
]