# Generated by Django 4.1.10 on 2023-08-11 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='duration',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
