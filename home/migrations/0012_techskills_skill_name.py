# Generated by Django 4.1 on 2022-10-16 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_techskills_skill_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='techskills',
            name='skill_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
