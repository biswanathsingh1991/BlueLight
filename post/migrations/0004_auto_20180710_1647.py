# Generated by Django 2.0.6 on 2018-07-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=0),
        ),
    ]
