# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanapp', '0003_auto_20160713_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hosts',
            name='enabled',
            field=models.CharField(default=b'UP', help_text='\u4e3b\u673a\u72b6\u6001UP\u4e3a\u542f\u52a8\uff0cDown\u4e3a\u6302\u8d77', max_length=10),
        ),
    ]
