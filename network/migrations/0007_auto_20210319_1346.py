# Generated by Django 3.1.5 on 2021-03-19 11:46

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20210319_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='Following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 19, 13, 46, 28, 755381)),
        ),
    ]
