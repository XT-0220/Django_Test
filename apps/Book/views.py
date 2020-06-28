from django.db.models import F, Q, Sum
from django.shortcuts import render # 渲染模板的方法
from django import http
from django.views import View
from Book.models import BookInfo, HeroInfo


class BookInfo2(View):

    def get(self,request):
        ################### 一对多关联查询 #################
        # 1.一查多：查询编号为1的图书中所有人物信息
        # # 先查询出一方模型对象
        # book = BookInfo.objects.get(id = 1)
        # 再使用一方模型对象调用关联的多方模型类名小写_set  (固定的语法)
        # hero = book.heroinfo_set.all()
        # print(hero)

        # 2.多查一：查询编号为1的英雄出自的书籍
        # 先查询出多方模型对象
        # hero = HeroInfo.objects.get(id=1)
        # 在使用多方模型对象调用多方模型类中的关联的外键属性名 (固定的语法)
        # book = hero.hbook
        # print(hero)

        ################### 排序查询 #################
        # 正序（默认）模型类.objects.filter('条件').order_by('模型属性')
        # 倒序：模型类.objects.filter('条件').order_by('-模型属性')

        # 查询书名不为空的图书，并且按照阅读量正序
        # 正序：升序，有小到大
        # books = BookInfo.objects.filter(btitle__isnull=False).order_by('bread')

        # 查询书名不为空的图书，并且按照阅读量倒序
        # 倒序：降序，有大到小
        # books = BookInfo.objects.filter(btitle__isnull=False).order_by('-bread')
        # print(books)

        ################## 聚合查询 #################
        # Avg 求平均值、Count 求数量、Max 求最大值、Min 求最小值、Sum 求和
        # 1.统计图书信息总的阅读量:对本表中所有的阅读量进行求和
        # ret = BookInfo.objects.aggregate(Sum('bread'))
        # ret = {'bread__sum': 146}
        # print(ret.get('bread__sum')) # ret['bread__sum']

        ################### F和Q查询 #################
        # F查询
        # 1.查询阅读量大于评论量的书籍
        # BookInfo.objects.filter(bread__gt=11)
        # book = BookInfo.objects.filter(bread__gt = F('bcomment'))
        # print(book)

        # Q查询：逻辑或、逻辑非
        # 先演示逻辑与：查询阅读量大于10，并且发布时间在1980年1月1号之后
        # book = BookInfo.objects.filter(bread__gt=10, bpub_date__gt='1980-1-1')
        # book = BookInfo.objects.filter(bread__gt=10, bpub_data__gt='1990-1-1')
        # print(book)

        # Q查询：逻辑或，给N个条件，只有有其中任何一个是满足的，都会被找到
        # 1.查询阅读量大于20，或编号小于3的图书
        # book = BookInfo.objects.filter(Q(bread__gt=20)|Q(id__lt = 3 ))
        # print(book)

        ################### 过滤查询 #################
        # 过滤查询的语法：模型类.objects.filter(属性__条件表达式=值)
        # 1.查询书名为'天龙八部'的书籍 (相等)
        # books = BookInfo.objects.filter(btitle__exact='天龙八部')
        # 判断相等的表达式可以简写的，而且是唯一可以简写的条件表达式
        # books = BookInfo.objects.filter(btitle='天龙八部')
        # print(books)

        # 2.查询书名包含'湖'的书籍 (模糊查询)
        # 原生SQL伪代码:select * from tb_bookinfo where btitle like %湖%
        # books = BookInfo.objects.filter(btitle__contains='湖')
        # print(books)

        # 3.查询书名以'部'结尾的书籍 (模糊查询) (endswith、startswith)
        # 原生SQL伪代码:select * from tb_bookinfo where btitle like %部
        # books = BookInfo.objects.filter(btitle__endswith='部')
        # print(books)

        # 4.查询书名不为空的书籍 (空查询)，特别特别容易出错
        # books = BookInfo.objects.filter(btitle__isnull=False)
        # print(books)

        # 5.查询编号为1或3或5的书籍 (范围查询)，特别容易误解
        # books = BookInfo.objects.filter(id__in=[1,3,5])
        # 查询编号为1或5的书籍 (范围查询)
        # books = BookInfo.objects.filter(id__in=[1,5])
        # print(books)

        # 6.查询编号大于3的书籍 (比较查询)
        # gt 大于 (greater than)
        # gte 大于等于 (greater than equal)
        # lt 小于 (less than)
        # lte 小于等于 (less than equal)
        # books = BookInfo.objects.filter(id__gt='3')
        # print(books)

        # 7. 查询id不等于3的书籍 (不相等)
        # exclude():跟filter一样的，也是一种过滤查询
        # exclude()：查询指定的条件以外的数据
        # filter()：查询满足指定条件的数据
        # books = BookInfo.objects.exclude(id=3)
        # print(books)

        # 8.查询1990年1月1日后发表的书籍
        # books = BookInfo.objects.filter(bpub_date__gt='1990-1-1')
        #
        # from datetime import date
        # books = BookInfo.objects.filter(bpub_date__gt=date(1990,1,1))
        # print(books)
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
        # book = BookInfo.objects.get(id = 5)
        # book.is_delete = True
        # book.save()

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


class TemView2(View):
        def get(self, request):
            # 查询所有图书信息
            books = BookInfo.objects.all()

            # 构造上下文
            context = {
                'books': books
            }
            # 使用上下文渲染'book.html'，并返回给客户端
            # return render(request, 'books.html', context)

            # 设置cookie:使用响应对象设置
            # 先创建出响应对象
            response = render(request, 'books.html', context)

            # 响应对象调用set_cookie()
            # response.set_cookie('username', '张小厨', max_age=3600) # 如果值为中文编码时会出错
            response.set_cookie('username', 'zxc', max_age=3600)

            # 设置session:假装登录后使用session记住用户登录状态
            # request.session['key'] = 'value'
            request.session['username'] = 'zxc'

            # 使用上下文字典渲染模板，并响应
            return response


class TestCookieView(View):

    def get(self, request):
        # 读取cookie
        username = request.COOKIES.get('username')
        print(username)

        # 使用cookie去辨别用户身份：Django框架中已经对此逻辑进行的封装，不需要我们做
        # 以下为伪代码：
        # user = 用户模型类.objects.get(username=username)
        # if user:
        # 用户是已登录的用户
        # else
        # 用户是未登录的用户

        return http.HttpResponse('测试Cookie')

class TestSessionView(View):
    """测试Session
    GET http://127.0.0.1:8000/session/
    """

    def get(self, request):
        # 读取session_data
        # request.session.get('key')
        username = request.session.get('username')
        print(username)

        # 使用session_data辨别用户身份:真实代码封装在AuthenticationMiddleware
        # 以下为伪代码：代码逻辑是类似的，只是Django存的是user_id
        # user = 用户模型类.objects.get(username=username)
        # if user:
        # 用户是已登录的用户
        # else
        # 用户是未登录的用户

        return http.HttpResponse('测试Session')
