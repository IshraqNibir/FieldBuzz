# Generated by Django 3.1 on 2020-12-11 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20201211_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='cv_file_tsync_id',
        ),
    ]