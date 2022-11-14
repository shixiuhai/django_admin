# Generated by Django 2.2.13 on 2021-03-06 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('username', models.CharField(max_length=32, verbose_name='用户')),
                ('view', models.CharField(max_length=32, verbose_name='视图')),
                ('desc', models.TextField(verbose_name='描述')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('detail', models.TextField(verbose_name='详情')),
            ],
            options={
                'verbose_name': '错误日志',
                'verbose_name_plural': '错误日志',
                'db_table': 'monitor_errorlogs',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='IpBlackList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name='IP')),
            ],
            options={
                'verbose_name': 'IP黑名单',
                'verbose_name_plural': 'IP黑名单',
                'db_table': 'monitor_ipblacklist',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='OnlineUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
            ],
            options={
                'verbose_name': '在线用户',
                'verbose_name_plural': '在线用户',
                'db_table': 'monitor_onlineusers',
                'ordering': ['-id'],
            },
        ),
    ]
