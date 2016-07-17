# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_type', models.IntegerField(default=0, choices=[(0, b'CMD'), (1, b'Login'), (2, b'Logout'), (3, b'GetFile'), (4, b'SendFile'), (5, b'exception')])),
                ('cmd', models.TextField()),
                ('memo', models.CharField(max_length=128, null=True, blank=True)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name': '\u5ba1\u8ba1\u65e5\u5fd7',
                'verbose_name_plural': '\u5ba1\u8ba1\u65e5\u5fd7',
            },
        ),
        migrations.CreateModel(
            name='BindHosts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u4e0e\u8fdc\u7a0b\u7528\u6237\u7ed1\u5b9a',
                'verbose_name_plural': '\u4e3b\u673a\u8fdc\u7a0b\u4e0e\u7528\u6237\u7ed1\u5b9a',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
                'verbose_name': '\u90e8\u95e8',
                'verbose_name_plural': '\u90e8\u95e8',
            },
        ),
        migrations.CreateModel(
            name='HostGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('memo', models.CharField(max_length=128, null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u7ec4',
                'verbose_name_plural': '\u4e3b\u673a\u7ec4',
            },
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(unique=True, max_length=64)),
                ('ip_addr', models.GenericIPAddressField(unique=True)),
                ('system_type', models.CharField(default=b'linux', max_length=32, choices=[(b'windows', b'Windows'), (b'linux', b'Linux/Unix')])),
                ('port', models.IntegerField(default=22)),
                ('enabled', models.BooleanField(default=True, help_text='\u4e3b\u673a\u82e5\u4e0d\u60f3\u88ab\u7528\u6237\u8bbf\u95ee\u53ef\u4ee5\u53bb\u6389\u6b64\u9009\u9879')),
                ('memo', models.CharField(max_length=128, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u4e3b\u673a',
                'verbose_name_plural': '\u4e3b\u673a',
            },
        ),
        migrations.CreateModel(
            name='HostUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth_method', models.CharField(help_text='\u5982\u679c\u9009\u62e9SSH/KEY\uff0c\u8bf7\u786e\u4fdd\u4f60\u7684\u79c1\u94a5\u6587\u4ef6\u5df2\u5728settings.py\u4e2d\u6307\u5b9a', max_length=16, choices=[(b'ssh-password', b'SSH/Password'), (b'ssh-key', b'SSH/KEY')])),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(help_text='\u5982\u679cauth_method\u9009\u62e9\u7684\u662fSSH/KEY,\u90a3\u6b64\u5904\u4e0d\u9700\u8981\u586b\u5199..', max_length=64, null=True, blank=True)),
                ('memo', models.CharField(max_length=128, null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u8fdc\u7a0b\u7528\u6237',
                'verbose_name_plural': '\u8fdc\u7a0b\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
                'verbose_name': 'IDC',
                'verbose_name_plural': 'IDC',
            },
        ),
        migrations.CreateModel(
            name='SessionTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('task_type', models.CharField(max_length=50, choices=[(b'cmd', b'CMD'), (b'file_send', b'\xe6\x89\xb9\xe9\x87\x8f\xe5\x8f\x91\xe9\x80\x81\xe6\x96\x87\xe4\xbb\xb6'), (b'file_get', b'\xe6\x89\xb9\xe9\x87\x8f\xe4\xb8\x8b\xe8\xbd\xbd\xe6\x96\x87\xe4\xbb\xb6')])),
                ('cmd', models.TextField()),
                ('expire_time', models.IntegerField(default=30)),
                ('task_pid', models.IntegerField(default=0)),
                ('note', models.CharField(max_length=100, null=True, blank=True)),
                ('hosts', models.ManyToManyField(to='taskmanapp.BindHosts')),
            ],
            options={
                'verbose_name': '\u6279\u91cf\u4efb\u52a1',
                'verbose_name_plural': '\u6279\u91cf\u4efb\u52a1',
            },
        ),
        migrations.CreateModel(
            name='TaskLogDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('event_log', models.TextField()),
                ('result', models.CharField(default=b'unknown', max_length=30, choices=[(b'success', b'Success'), (b'failed', b'Failed'), (b'unknown', b'Unknown')])),
                ('note', models.CharField(max_length=100, blank=True)),
                ('bind_host', models.ForeignKey(to='taskmanapp.BindHosts')),
                ('child_of_task', models.ForeignKey(to='taskmanapp.TaskLog')),
            ],
            options={
                'verbose_name': '\u6279\u91cf\u4efb\u52a1\u65e5\u5fd7',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test', models.CharField(max_length=32)),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=64)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expire', models.IntegerField(default=300)),
                ('host', models.ForeignKey(to='taskmanapp.BindHosts')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('valid_begin_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_end_time', models.DateTimeField()),
                ('bind_hosts', models.ManyToManyField(to='taskmanapp.BindHosts', verbose_name='\u6388\u6743\u4e3b\u673a', blank=True)),
                ('department', models.ForeignKey(verbose_name='\u90e8\u95e8', to='taskmanapp.Department')),
                ('host_groups', models.ManyToManyField(to='taskmanapp.HostGroups', verbose_name='\u6388\u6743\u4e3b\u673a\u7ec4', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CrazyEye\u8d26\u6237',
                'verbose_name_plural': 'CrazyEye\u8d26\u6237',
            },
        ),
        migrations.AddField(
            model_name='token',
            name='user',
            field=models.ForeignKey(to='taskmanapp.UserProfile'),
        ),
        migrations.AddField(
            model_name='tasklog',
            name='user',
            field=models.ForeignKey(to='taskmanapp.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='hostusers',
            unique_together=set([('auth_method', 'password', 'username')]),
        ),
        migrations.AddField(
            model_name='hosts',
            name='idc',
            field=models.ForeignKey(to='taskmanapp.IDC'),
        ),
        migrations.AddField(
            model_name='bindhosts',
            name='host',
            field=models.ForeignKey(to='taskmanapp.Hosts'),
        ),
        migrations.AddField(
            model_name='bindhosts',
            name='host_group',
            field=models.ManyToManyField(to='taskmanapp.HostGroups'),
        ),
        migrations.AddField(
            model_name='bindhosts',
            name='host_user',
            field=models.ForeignKey(to='taskmanapp.HostUsers'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='host',
            field=models.ForeignKey(to='taskmanapp.BindHosts'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='session',
            field=models.ForeignKey(to='taskmanapp.SessionTrack'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='user',
            field=models.ForeignKey(to='taskmanapp.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='bindhosts',
            unique_together=set([('host', 'host_user')]),
        ),
    ]
