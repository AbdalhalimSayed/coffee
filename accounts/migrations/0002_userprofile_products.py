# Generated by Django 5.0.6 on 2024-06-27 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('products', '0005_alter_product_publishdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='products',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
