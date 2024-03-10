# Generated by Django 4.1.7 on 2023-03-25 14:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.TextField(default='')),
                ('biography', models.TextField(default='')),
                ('what_we_believe', models.TextField(default='')),
                ('vision', models.TextField(default='')),
                ('service_times', models.TextField(default='')),
                ('ministry_name', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
                ('caption_text', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EnglishAudioSermons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=200)),
                ('audio', models.FileField(null=True, upload_to='audio_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['wav', 'mp3', 'AIFF', 'aac', 'ogg', 'm4a'])])),
                ('pastor_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('images', models.FileField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='LugandaAudioSermons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=200)),
                ('audio', models.FileField(null=True, upload_to='audio_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['wav', 'mp3', 'AIFF', 'aac', 'ogg', 'm4a'])])),
                ('pastor_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MinistryName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ministryName', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='OngoingProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video', models.FileField(default='', null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('details', models.TextField()),
                ('coverphoto', models.ImageField(null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='OurHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='OurStaffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_image', models.ImageField(upload_to='media')),
                ('member_title', models.CharField(max_length=200)),
                ('member_name', models.CharField(max_length=200)),
                ('member_biography', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quote', models.TextField()),
                ('From', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Servicetimes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicetimes', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='VideoBanners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
            ],
        ),
        migrations.CreateModel(
            name='VideoSermons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverphoto', models.ImageField(upload_to='media')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=200)),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('pastor_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vision', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Whatwebelieve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_we_believe', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(null=True, upload_to='media')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainApp.ongoingprojects')),
            ],
        ),
    ]
