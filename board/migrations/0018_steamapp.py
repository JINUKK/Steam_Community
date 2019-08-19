# Generated by Django 2.2.4 on 2019-08-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0017_auto_20190705_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='SteamApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.PositiveIntegerField(db_index=True, unique=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('image', models.TextField(blank=True)),
                ('discount_per', models.PositiveIntegerField(default=0)),
                ('init_price', models.CharField(blank=True, max_length=10)),
                ('final_price', models.CharField(blank=True, max_length=10)),
                ('developer', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('coming_soon', models.BooleanField(default=False)),
                ('release_date', models.CharField(blank=True, max_length=30)),
                ('supported_languages', models.CharField(max_length=200)),
            ],
        ),
    ]