# Generated by Django 3.1 on 2020-12-11 14:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20201211_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='tsync_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
