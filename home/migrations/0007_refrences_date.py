# Generated by Django 4.1 on 2022-10-15 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_refrences'),
    ]

    operations = [
        migrations.AddField(
            model_name='refrences',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
