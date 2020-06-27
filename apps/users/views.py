from django import http
from django.shortcuts import render


# Create your views here.
# def register(request):
#
#     return http.HttpResponse('注册')
from django.views import View


class RegisterView(View):

    def get(self, request):

        return http.HttpResponse('1')

    def post(self,request):

        return http.HttpResponse('2')


class LoginView(View):

    def get(self,request):

        return http.HttpResponse('3')

# 测试路由屏蔽

class HelView(View):

    def get(self,request):

        return http.HttpResponse('hHello!!!')

class HelloView(View):

    def get(self,request):

        return http.HttpResponse('Hello!!!')


