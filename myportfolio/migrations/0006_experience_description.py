# Generated by Django 4.1.10 on 2023-08-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0005_remove_projects_title_projects_associated_with_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
