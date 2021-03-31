# Generated by Django 3.1.6 on 2021-02-17 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='remark',
            new_name='dest_file_location',
        ),
        migrations.RemoveField(
            model_name='file',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='file',
            name='dest_ip',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='hostname',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]