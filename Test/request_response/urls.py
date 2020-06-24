from django.urls import path, re_path
from . import views

urlpatterns = [
    # 查询字符串
    path('querystring/',views.QSparamView.as_view()),

    path('formdata/', views.FormDataParamView.as_view()),

    path('json/',views.JsonParamView.as_view()),

    path('urlparam/<int:num>',views.URLparamView.as_view()),

    path('urlparam2/<mobile:Phone_num>',views.URLparam2View.as_view()),

    re_path(r'urlparam3/?p<mobile_num>(1[3-9]\d{9})$',views.URLparam3View.as_view())

]

