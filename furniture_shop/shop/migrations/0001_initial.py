# Generated by Django 3.0.6 on 2020-05-15 00:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('cost', models.FloatField()),
                ('description', models.TextField()),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to='product_pics'), size=None)),
            ],
        ),
    ]
