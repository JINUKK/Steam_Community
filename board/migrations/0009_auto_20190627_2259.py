# Generated by Django 2.2.1 on 2019-06-27 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='app_image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='app_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='app_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='app_price',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]