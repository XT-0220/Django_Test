from django.urls import path

from Book import views

urlpatterns = [

    path('test/',views.BookInfo1.as_view()),
]



