# Generated by Django 4.1 on 2022-10-14 17:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_socialicons_icon_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techskills',
            name='skill_desc',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
