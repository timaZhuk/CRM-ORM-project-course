# Generated by Django 5.1.3 on 2024-11-17 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_comment_todolist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
    ]
