# Generated by Django 2.2.1 on 2019-06-13 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
