# Generated by Django 3.1.5 on 2021-04-06 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_auto_20210406_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 13, 50, 11, 657108)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='like',
            field=models.ManyToManyField(blank='True', to='network.Profile'),
        ),
    ]