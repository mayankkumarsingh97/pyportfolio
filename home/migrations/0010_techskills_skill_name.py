# Generated by Django 4.1 on 2022-10-16 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_contactus_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='techskills',
            name='skill_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
