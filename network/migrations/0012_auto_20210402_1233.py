# Generated by Django 3.1.5 on 2021-04-02 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_auto_20210331_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 2, 12, 33, 22, 748000)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='like',
            field=models.ManyToManyField(blank='True', to='network.Profile'),
        ),
    ]
