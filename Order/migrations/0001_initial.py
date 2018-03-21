# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-17 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Shoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('tel', models.CharField(max_length=20, verbose_name='电话')),
                ('wechat', models.CharField(blank=True, max_length=20, verbose_name='微信')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='订单提交时间')),
            ],
            options={
                'verbose_name_plural': '订单',
                'verbose_name': '订单',
            },
        ),
        migrations.CreateModel(
            name='Buyer_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': '订单类别',
                'verbose_name': '订单类别',
            },
        ),
        migrations.AddField(
            model_name='buyer',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Order.Buyer_category', verbose_name='订单状态'),
        ),
        migrations.AddField(
            model_name='buyer',
            name='shoes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shoes.Shoes', verbose_name='购买的鞋子'),
        ),
    ]
