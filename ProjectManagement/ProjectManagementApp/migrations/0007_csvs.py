# Generated by Django 4.0.1 on 2022-02-09 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManagementApp', '0006_remove_projects_assigned_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csvs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
