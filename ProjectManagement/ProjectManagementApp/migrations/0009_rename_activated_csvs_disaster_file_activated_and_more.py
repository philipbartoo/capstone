# Generated by Django 4.0.1 on 2022-02-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManagementApp', '0008_csvs_activated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csvs',
            old_name='activated',
            new_name='disaster_file_activated',
        ),
        migrations.RenameField(
            model_name='csvs',
            old_name='uploaded',
            new_name='disaster_file_uploaded',
        ),
        migrations.RemoveField(
            model_name='csvs',
            name='file_name',
        ),
        migrations.AddField(
            model_name='csvs',
            name='disaster_file_name',
            field=models.FileField(default='abc', upload_to='disaster_files/'),
            preserve_default=False,
        ),
    ]
