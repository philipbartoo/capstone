# Generated by Django 4.0.1 on 2022-02-10 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManagementApp', '0011_remove_csvs_disaster_file_activated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvs',
            name='disaster_file',
            field=models.FileField(upload_to='disasters/'),
        ),
    ]
