# Generated by Django 5.0.6 on 2024-06-27 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_products_userprofile_favoriteproducts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='favoriteProducts',
        ),
    ]
