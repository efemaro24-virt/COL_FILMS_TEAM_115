# Generated by Django 4.0.6 on 2022-08-03 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_alter_upload_id_alter_upload_video_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='no_of_reacts',
            field=models.IntegerField(default=0),
        ),
    ]