# Generated by Django 3.1 on 2020-12-14 09:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_candidate_cv_file_tsync_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='cv_file_tsync_id',
            field=models.UUIDField(default=uuid.uuid1, editable=False, unique=True),
        ),
    ]
