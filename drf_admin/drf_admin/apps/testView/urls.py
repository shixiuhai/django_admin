""" 
@author: Wang Meng
@github: https://github.com/tianpangji 
@software: PyCharm 
@file: urls.py 
@create: 2020/6/21 22:28
"""
from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token

from testView.views import TestView

urlpatterns = [
    path('', TestView.as_view()),
   
]
