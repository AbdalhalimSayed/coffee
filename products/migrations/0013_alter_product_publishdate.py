# Generated by Django 5.0.6 on 2024-06-27 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_publishdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='publishDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 27, 19, 10, 51, 317222)),
        ),
    ]
