"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

# 调用注册路由转换器的方法,完成路由转换器的注册
# ﻿就是将自定义的路由转换器，添加到路由转换器容器中：REGISTERED_CONVERTERS={}  (源代码有体现)
# register_converter('自定义的路由转换器类', '别名')
from django.urls.converters import register_converter
from converters import MobileConverter

register_converter(MobileConverter, 'mobile')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('users.urls')),

    path('', include('request_response.urls')),

    path('', include(('request_response.urls', 'request_response'), namespace='request_response')),

]
