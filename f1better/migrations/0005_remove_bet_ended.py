# Generated by Django 2.0 on 2018-01-12 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f1better', '0004_race_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='ended',
        ),
    ]