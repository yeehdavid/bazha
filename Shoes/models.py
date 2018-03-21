from django.db import models
from django.urls import reverse
# Create your models here.

class Brand(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = '品牌'
        verbose_name_plural='品牌'

class Shoes(models.Model):
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('Main:detail', kwargs={'pk': self.pk})
    name = models.CharField(max_length=100,verbose_name='商品名称')
    desc = models.CharField(max_length=100 ,blank=True,verbose_name='商品描述')
    brand = models.ForeignKey(Brand,verbose_name='品牌')
    price = models.IntegerField(default=99999,verbose_name='价格')
    img_title = models.ImageField(upload_to='Shoes',blank=True,verbose_name='标题图片')
    img0 = models.ImageField(upload_to='Shoes',blank=True,verbose_name='图片一')
    img1 = models.ImageField(upload_to='Shoes',blank=True,verbose_name='图片二')
    img2 = models.ImageField(upload_to='Shoes',blank=True,verbose_name='图片三')
    img3 = models.ImageField(upload_to='Shoes',blank=True,verbose_name='图片四')
    img4 = models.ImageField(upload_to='Shoes',blank=True,verbose_name='图片五')
    img5 = models.ImageField(upload_to='Shoes',blank=True,verbose_name='图片六')
    img6 = models.ImageField(upload_to='Shoes',blank=True,verbose_name='图片七')
    img7 = models.ImageField(upload_to='Shoes',blank=True,verbose_name='图片八')
    img8 = models.ImageField(upload_to='Shoes',blank=True,verbose_name='图片九')

    class Meta:

        verbose_name = '鞋子'
        verbose_name_plural='鞋子'