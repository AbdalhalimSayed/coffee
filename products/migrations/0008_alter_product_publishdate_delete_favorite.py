# Generated by Django 5.0.6 on 2024-06-27 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_publishdate_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='publishDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 27, 17, 47, 37, 725181)),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
