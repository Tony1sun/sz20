from django.db import models

# Create your models here.
class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)
    # btitle = models.CharField(max_length=20, unique=True)
    #价格，最大位数为16，小数为2
    # bprice = models.DecimalField(max_digits=10,
    #         decimal_places=2)
    #出版日期
    bpub_date = models.DateField()
    #阅读量
    bread = models.IntegerField(default=0)
    #评论量
    bcomment = models.IntegerField(default=0)
    #删除标记
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    '''英雄名字'''
    hname = models.CharField(max_length=20)
    #性别
    hgender = models.BooleanField(default=False)
    #备注
    hcomment = models.CharField(max_length=200, null=True,
                                blank=True)
    #关系属性
    hbook = models.ForeignKey('BookInfo')
    #删除标记
    isDelete = models.BooleanField(default=False)


#新闻类型类
class NewsType(models.Model):
    #新闻类型
    type_name = models.CharField(max_length=20)
    #关系属性
    type_news = models.ManyToManyField('NewsInfo')

#新闻类
class NewsInfo(models.Model):
    #新闻标题
    title =  models.CharField(max_length=128)
    #发布时间
    pub_date = models.DateTimeField(auto_now_add=True)
    #信息内容
    content = models.TextField()
    #关系属性
    news_type = models.ManyToManyField('NewsType')


class EmployeeBasicInfo(models.Model):
    #姓名
    name = models.CharField(max_length=20)
    #性别
    gender = models.BooleanField(default=False)
    #年龄
    age = models.IntegerField()
    #关系属性
    employee_basic = models.OneToOneField('EmployeeDetailInfo')

#员工详细信息类
class EmployeeDetailInfo(models.Model):
    #联系地址
    addr = models.CharField(max_length=256)
    #关系属性
    # employee_basic = models.OneToOneField('EmployeeBasicInfo')
