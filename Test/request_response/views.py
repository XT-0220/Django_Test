from django import http
from django.shortcuts import render

# Create your views here.
from django.views import View


class QSparamView(View):

    def get(self,request):

        name = request.GET.get('name','XT')
        age = request.GET.get('age',20)

        # return http.HttpResponse('查询字符串参数：%s--%s' % (name , age))

        return http.HttpResponse('查询字符串参数：%s--%s' % (name, age))

    # def get(self, request):
    #     """
    #     从请求对象中提取查询字符串参数name、age
    #     request.GET：专门用于提取请求地址中的查询字符串参数的
    #     注意点：
    #         在提取查询字符串参数时，跟请求方式没有任何的关系，
    #         即任何请求方式，只要传递了查询字符串都是使用request.GET
    #     :param request: 请求对象
    #     :return: 响应对象
    #     """
    #     # query_str_param = request.GET
    #     # name = query_str_param.get('name')
    #     name = request.GET.get('name')
    #     age = request.GET.get('age')
    #     print(name, age)
    #
    #     return http.HttpResponse('GET 测试提取查询字符串')
    #
    # def post(self, request):
    #     name = request.GET.get('name')
    #     age = request.GET.get('age')
    #     print(name, age)
    #
    #     return http.HttpResponse('POST 测试提取查询字符串')

class FormDataParamView(View):

    def post(self,request):

        username = request.POST.get('username')
        password = request.POST.get('password')

        return http.HttpResponse('表单类型请求体参数：%s--%s' % (username, password))