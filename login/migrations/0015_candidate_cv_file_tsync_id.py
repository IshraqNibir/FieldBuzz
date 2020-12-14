# Generated by Django 3.1 on 2020-12-14 08:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20201212_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='cv_file_tsync_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
