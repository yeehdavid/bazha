from django.db import models
import datetime
from django.urls import reverse
# Create your models here.

class Article(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200,verbose_name='文章标题')
    title_img = models.CharField(max_length=200,blank=True,verbose_name='文章标题图片')
    created_time = models.DateTimeField(default=datetime.datetime.now,verbose_name='发布时间')

    def get_absolute_url(self):
        return reverse('News:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = '文章'
        verbose_name_plural='文章'


class Article_Part(models.Model):
    def __str__(self):
        return self.text
    text = models.TextField(blank=True)
    img = models.ImageField(upload_to='News', blank=True)
    belong_to = models.ForeignKey(Article)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = '文章内容'
        verbose_name_plural = '文章内容'