from django.urls import path

from Book import views

urlpatterns = [

    path('test1/',views.BookInfo1.as_view()),

    path('test2/',views.BookInfo2.as_view()),

    path('tem/',views.TemView.as_view()),
]



