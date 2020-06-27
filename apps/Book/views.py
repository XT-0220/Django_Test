from django.db.models import F, Q, Sum
from django.shortcuts import render # 渲染模板的方法
from django import http
from django.views import View
from Book.models import BookInfo, HeroInfo


class BookInfo2(View):

    def get(self,request):

        ################### 基本查询 #################
        # 1. 查询指定记录：只查询第一条记录
        # 如果只查一条记录，优先选择get()，默认只查一条记录
        # book = BookInfo.objects.get(id = 1)
        # print(book)

        # 2. 查询表中所有记录
        # book = BookInfo.objects.all()
        # print(book)

        # 3. 查询记录的个数：查询表中所有记录的个数
        # book = BookInfo.objects.all().count()
        # print(book)

        # 4.查询记录的个数：查询满足条件记录个数，查询未被逻辑删除的记录的个数
        # count = BookInfo.objects.filter(  is_delete = True  ).count()
        # print(count)

        return http.HttpResponse('测试查询')


class BookInfo1(View):

    def get(self,request):
        ################### is_delete逻辑删除记录 #################
        book = BookInfo.objects.get(id = 5)
        book.is_delete = True
        book.save()

        ################### delete()方法物理删除记录 #################
        # 语法：模型类.objects.filter('条件').delete()
        # BookInfo.objects.filter(id = 6).delete()

        ################### update()方法修改记录 #################
        # 语法：模型类.objects.filter('条件').update(模型属性=新值)
        # BookInfo.objects.filter(id = 6).update(btitle = '西游记后传')

        ################### save()方法修改记录 #################
        # book = BookInfo.objects.get(id = 6)
        # book.btitle = '西游记'
        # book.save()

        ################### create()方法新增记录 #################
        # 语法：模型类.模型管理器.create(模型属性=值)
        # 模型管理器：是由Django提供并封装的一个对象（objects），用于调用ORM的接口方法，固定的语法
        # BookInfo.objects.create(
        # btitle = '西游记1',
        # bread = 10,
        # bpub_data= '2020-5-20',
        # bcomment = 1111
        # )

        ################### save()方法新增记录 #################

        # # 注意点：逻辑删除在新增时不要赋值
        # # book.is_delete = False、True
        #
        # # 使用模型对象调用save()
        # # save()：它是将模型对象属性中的值，同步到对应的数据表的字段中
        # book.save()


        # book = BookInfo()
        #
        # book.btitle = '西游记'
        # book.bread = 10
        # book.bpub_data= '2020-5-20'
        # book.bcomment = 1111
        #
        # book.save()

        return http.HttpResponse('测试1')

# 测试模板的定义和响应
class TemView(View):

    def get(self,request):
        # 假装在处理逻辑......

        # 构造上下文字典：将上下文字典中的数据渲染到HTML模板文件
        context = {
            # 'key': 'value'
            'subject': 'Python学科',
            'hot': '真的牛逼'
        }

        # 响应结果：模板（html文件）
        # render()使用上下文字典渲染模板
        return render(request,'temp.html',context)