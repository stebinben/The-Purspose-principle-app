# Generated by Django 2.0.2 on 2019-05-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_title1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title1',
        ),
        migrations.AddField(
            model_name='product',
            name='body',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]
