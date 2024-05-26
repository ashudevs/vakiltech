# Generated by Django 3.1.7 on 2024-05-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20240524_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ScrapedData',
        ),
    ]
