from app1.views import *
from django.urls import path
app_name='app1'
urlpatterns=[
    path('file1/',file1,name='file1'),
]