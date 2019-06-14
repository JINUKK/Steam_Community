from django.urls import path
from .views import *
urlpatterns = [
    path('accounts/login', Login.as_view(), name='account_login'),
]