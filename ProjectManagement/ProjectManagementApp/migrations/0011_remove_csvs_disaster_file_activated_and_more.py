# Generated by Django 4.0.1 on 2022-02-09 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManagementApp', '0010_rename_disaster_file_name_csvs_disaster_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvs',
            name='disaster_file_activated',
        ),
        migrations.RemoveField(
            model_name='csvs',
            name='disaster_file_uploaded',
        ),
        migrations.AlterField(
            model_name='csvs',
            name='disaster_file',
            field=models.FileField(upload_to=''),
        ),
    ]
