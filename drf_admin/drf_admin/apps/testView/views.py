from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import  AllowAny
class TestView(APIView):
    # permission_classes=[AllowAny]
    def get(self,request):
        return Response("成功")

