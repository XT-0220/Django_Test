from django import http
from django.views import View
from Book.models import BookInfo

class BookInfo1(View):

    def get(self,request):
        ################### is_delete逻辑删除记录 #################






        ################### delete()方法物理删除记录 #################









        ################### update()方法修改记录 #################





        ################### save()方法修改记录 #################



        ################### create()方法新增记录 #################
        # BookInfo.objects.create(
        # btitle = '西游记1',
        # bread = 10,
        # bpub_data= '2020-5-20',
        # bcomment = 1111
        # )

        ################### save()方法新增记录 #################
        # book = BookInfo()
        #
        # book.btitle = '西游记'
        # book.bread = 10
        # book.bpub_data= '2020-5-20'
        # book.bcomment = 1111
        #
        # book.save()

        return http.HttpResponse('测试1')