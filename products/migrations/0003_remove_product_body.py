# Generated by Django 2.0.2 on 2019-05-18 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190518_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='body',
        ),
    ]
