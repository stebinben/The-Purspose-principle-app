# Generated by Django 2.0.2 on 2019-05-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20190518_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.CharField(default='string2', max_length=125),
        ),
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.CharField(default='STRING', max_length=120),
        ),
    ]