# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 04:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('hostname', models.CharField(max_length=40, verbose_name='主机名称')),
                ('num', models.CharField(max_length=20, verbose_name='编号')),
                ('application', models.CharField(max_length=40, verbose_name='应用')),
            ],
            options={
                'verbose_name_plural': '主机列表',
                'verbose_name': '主机列表',
            },
        ),
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=40, verbose_name='厂商')),
                ('productmode', models.CharField(max_length=40, verbose_name='产品型号')),
                ('serialnumber', models.CharField(max_length=40, verbose_name='产品序列号')),
                ('cpu', models.CharField(blank=True, max_length=40, null=True, verbose_name='CPU核数')),
                ('mem', models.CharField(max_length=40, verbose_name='内存')),
                ('os', models.CharField(max_length=40, verbose_name='操作系统')),
                ('disk', models.CharField(max_length=40, verbose_name='硬盘大小')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Host')),
            ],
            options={
                'verbose_name_plural': '主机信息',
                'verbose_name': '主机信息',
            },
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='机房名称')),
                ('remark', models.CharField(max_length=50, verbose_name='备注')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '机房',
                'verbose_name': '机房',
            },
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(verbose_name='ip')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Host')),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Idc'),
        ),
    ]