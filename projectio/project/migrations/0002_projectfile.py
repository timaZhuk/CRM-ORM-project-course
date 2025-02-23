# Generated by Django 5.1.3 on 2024-11-25 16:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('attachment', models.FileField(upload_to='projectfiles')),
            ],
        ),
    ]
