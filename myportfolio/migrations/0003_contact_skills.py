# Generated by Django 4.1.10 on 2023-08-11 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_projects_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='skills',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]