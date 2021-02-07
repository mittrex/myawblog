# Generated by Django 3.1.6 on 2021-02-07 03:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=40)),
                ('post_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('post_text', models.CharField(max_length=1000)),
                ('post_image', models.ImageField(upload_to='blog_images/')),
            ],
        ),
    ]