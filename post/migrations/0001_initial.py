# Generated by Django 2.0.6 on 2018-07-07 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biswanath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=204)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_like', models.BooleanField(default=False)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('containt', models.CharField(blank=True, max_length=99999999, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Post/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now=True)),
                ('userprofile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_comment', models.CharField(blank=True, max_length=999999, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('post', models.ManyToManyField(to='post.Post')),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='core.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
        migrations.AddField(
            model_name='like',
            name='userprofile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='post_like', to='core.UserProfile'),
        ),
    ]
