# Generated by Django 4.1 on 2022-10-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_mywork_date_techskills_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(blank=True, max_length=70, unique=True, verbose_name='Email'),
        ),
    ]
