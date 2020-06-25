import json
from django.views import View
from django import http
from django.shortcuts import render, redirect , reverse

# Create your views here.



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


class JsonParamView(View):

    def post(self,request):

        json_str = request.body

        json_dict = json.loads(json_str)

        username = json_dict.get('username')
        password = json_dict.get('password')

        return http.HttpResponse('非表单类型请求体参数：%s--%s' % (username, password))

class URLparamView(View):

    def get(self, request, num):

        return http.HttpResponse('test: %s ' % num)


class URLparam2View(View):
    """测试path()中自定义路由转换器提取路径参数：手机号
    http://127.0.0.1:8000/url_param2/18500001111/
    """

    def get(self, request,Phone_num):
        """
        :param phone_num: 路由提取的关键字参数
        """
        return http.HttpResponse('测试path()提取路径参数手机号：%s',Phone_num)

class URLparam3View(View):

    def get(self,request,mobile_num):

        return http.HttpResponse('测试path()提取路径参数手机号：%s' % mobile_num)


class Response1View(View):
    """测试HttpResponse
       http://127.0.0.1:8000/response1/
       """

    def get(self, request):
        # 使用HttpResponse构造响应数据
        # return http.HttpResponse(content='itcast python', status=200)
        # 可简写
        # return http.HttpResponse('itcast python')

        # 另外一种写法
        response = http.HttpResponse('itcast python')
        return response

class JSONResponseView(View):
    """测试JSONResponse
    http://127.0.0.1:8000/json_resp/
    """

    def get(self, request):
        # 准备要响应的数据
        dict_data = {
            'city': 'beijing',
            'subject': 'python'
        }
        # 使用JSONResponse构造并响应JSON数据
        return http.JsonResponse(dict_data)

class IndexView(View):

    def get(self,request):

        return http.HttpResponse('首页')

class  LoginRedictView(View):

    def post(self,request):

        # return redirect('http://127.0.0.1:8000/index/')
        return redirect(reverse('request_response.urls','index'))