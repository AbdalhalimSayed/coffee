# Generated by Django 5.0.6 on 2024-06-20 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('photo', models.ImageField(upload_to='Photo/%y/%m/%d')),
                ('is_active', models.BooleanField(default=False)),
                ('publishDate', models.DateTimeField(default=datetime.datetime(2024, 6, 20, 19, 5, 24, 936562))),
            ],
        ),
    ]
