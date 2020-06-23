from django.urls import path, re_path

from . import views

urlpatterns = [

    path('users/register', views.RegisterView.as_view()),

    re_path(r'^users/login/$', views.LoginView.as_view()),

    # 测试路由屏蔽
    re_path(r'^Hel', views.HelView.as_view()),

    re_path(r'^Hello', views.HelloView.as_view()),



]