# Generated by Django 4.1.7 on 2023-03-14 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_image_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='images',
        ),
    ]
