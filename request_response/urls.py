from django.urls import path, re_path
from . import views

urlpatterns = [
    # 查询字符串
    path('querystring/',views.QSparamView.as_view()),

    path('formdata/', views.FormDataParamView.as_view()),

    path('json/',views.JsonParamView.as_view()),

    path('urlparam/<int:num>',views.URLparamView.as_view()),

    path('urlparam2/<mobile:Phone_num>/',views.URLparam2View.as_view()),

    re_path(r'urlparam3/(?P<mobile_num>1[3-9]\d{9})/$',views.URLparam3View.as_view()),

    path('response1/', views.Response1View.as_view()),

    # 测试JSONResponse：http://127.0.0.1:8000/json_resp/
    path('json_resp/', views.JSONResponseView.as_view()),

    path('index/',views.IndexView.as_view()),

    path('login_redirect/',views.LoginRedictView.as_view()),

    re_path(r'URLParam4/(?P<QQ_num>2[0-9]\d{8})/$',views.URLParamView4.as_view()),
]


