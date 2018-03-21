from django.db import models

class Buyer_category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20)
    class Meta:
        verbose_name = '订单类别'
        verbose_name_plural='订单类别'
class Buyer(models.Model):
    def __str__(self):
        return self.name
    shoes = models.ForeignKey('Shoes.Shoes',verbose_name='购买的鞋子')
    name = models.CharField(max_length=20,verbose_name='姓名')
    address = models.CharField(max_length=100,verbose_name='地址')
    tel = models.CharField(max_length=20,verbose_name='电话')
    wechat = models.CharField(max_length=20,blank=True,verbose_name='微信')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='订单提交时间')
    category = models.ForeignKey(Buyer_category,default=1,verbose_name='订单状态')
    class Meta:
        verbose_name = '订单'
        verbose_name_plural='订单'
# Create your models here.
