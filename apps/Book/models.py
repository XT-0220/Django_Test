from django.db import models

# Create your models here.

"""
定义模型属性，映射数据表字段
字段有哪些，属性就有哪些，其中，默认的id主键不需要处理
字段类型是什么，属性就指定对应的类型
字段约束条是什么，属性就指定对应的约束条件
"""

class BookInfo(models.Model):
    btitle = models.CharField(max_length=64,verbose_name='书名')
    bpub_data = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0,verbose_name='阅读量')
    bcomment = models.IntegerField(default=0,verbose_name='评论量')
    is_delete = models.BooleanField(default=False,verbose_name="逻辑删除")

    class Meta:
        db_table = 'tb_bookinfo'




class HeroInfo(models.Model):

    GENDER_CHOICES = (
        (0,'female'),
        (1,'male')
    )

    hbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='英雄属于你的图书')
    hname = models.CharField(max_length=20,verbose_name='人名')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES,default=0,verbose_name='性别')
    hcomment = models.CharField(max_length=200,null=True,verbose_name='描述信息')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heroinfo'

