# Generated by Django 4.1.10 on 2023-08-11 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0003_contact_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('issuer', models.CharField(max_length=100)),
                ('issuedDate', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('link', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]