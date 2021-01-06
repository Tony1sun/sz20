from django.db import models

class BookInfoManager(models.Manager):
    '''图书模型管理器类'''
    #改变查询结果集
    def all(self):
        #调用父类的all，获取所有数据
        books = super().all()
        #对数据进行过滤
        books = books.filter(isDelete=False)
        #返回
        return books

    #封装函数:操作模型类对应的数据表(增删改查)
    def create_book(self, btitle, bpub_date):
        #创建一个图书对象
        #获取self所在的模型类
        model_class = self.model
        book = model_class()
        # book = BookInfo()
        book.btitle = btitle
        book.bpub_date = bpub_date
        #保存进数据库
        book.save()
        #返回book
        return book

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
    #自定义一个Manager类对象
    book = models.Manager()
    objects = BookInfoManager() #自定义一个BookInfoManger类的对象

    # @classmethod
    # def create_book(cls, btitle, bpub_date):
    #     #创建一个图书对象
    #     obj = cls()
    #     obj.btitle = btitle
    #     obj.bpub_date = bpub_date
    #     #保存到数据库
    #     obj.save()
    #     return obj

    class Meta:
        db_table = 'bookinfo' #指定模型类对应的表名


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
    # news_type = models.ManyToManyField('NewsType')

#员工基本信息类
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

class AreaInfo(models.Model):
    '''地区模型类'''
    #地区
    atitle = models.CharField(max_length=20)
    #关系属性'代表当前地区的父级地区
    aParent = models.ForeignKey('self', null=True, blank=True)

