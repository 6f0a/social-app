# Generated by Django 3.1.5 on 2021-04-05 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_auto_20210402_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 5, 14, 41, 52, 730960)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='like',
            field=models.ManyToManyField(blank='True', to='network.Profile'),
        ),
    ]
