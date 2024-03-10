# Generated by Django 4.1.7 on 2023-03-25 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_ministries'),
    ]

    operations = [
        migrations.AddField(
            model_name='ministryname',
            name='image',
            field=models.FileField(default='', upload_to='media'),
        ),
        migrations.AddField(
            model_name='ourhistory',
            name='image',
            field=models.FileField(default='', upload_to='media'),
        ),
        migrations.AddField(
            model_name='vision',
            name='image',
            field=models.FileField(default='', upload_to='media'),
        ),
        migrations.AddField(
            model_name='whatwebelieve',
            name='image',
            field=models.FileField(default='', upload_to='media'),
        ),
    ]