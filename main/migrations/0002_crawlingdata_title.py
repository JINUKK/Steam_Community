# Generated by Django 2.2.1 on 2019-08-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawlingdata',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]