# Generated by Django 3.0.7 on 2020-06-23 02:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('added_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField(unique=True)),
                ('added_on', models.DateTimeField(default=datetime.datetime.now)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trackalbum', to='library.Album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trackartist', to='library.Artist')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracklanguage', to='library.Language')),
            ],
        ),
    ]