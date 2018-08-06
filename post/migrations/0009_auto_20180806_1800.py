# Generated by Django 2.1 on 2018-08-06 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20180725_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post_like',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
