from django.urls import path

from .views import rank_list, rank_pause

app_name = 'main'

urlpatterns = [
    path('', rank_pause, name = 'ranklist'),
]