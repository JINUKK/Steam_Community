# Generated by Django 2.2.1 on 2019-06-18 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated',
        ),
    ]
