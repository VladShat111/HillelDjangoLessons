# Generated by Django 2.1.3 on 2018-12-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deskoffile',
            name='fileForDownload',
            field=models.FileField(blank=True, upload_to='file'),
        ),
    ]
