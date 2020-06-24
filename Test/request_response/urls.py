from django.urls import path
from . import views

urlpatterns = [
    # 查询字符串
    path('querystring/',views.QSparamView.as_view()),

    path('formdata/', views.FormDataParamView.as_view()),

    path('json/',views.JsonParamView.as_view()),

]

