# Generated by Django 4.1 on 2022-10-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='socialicons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_image', models.FileField(null=True, upload_to='uploads/')),
                ('icon_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]