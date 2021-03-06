# Generated by Django 2.0 on 2018-01-12 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ended', models.BooleanField(default=False)),
                ('money', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=250)),
                ('multiplier', models.DecimalField(decimal_places=1, max_digits=6)),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RaceDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f1better.Driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f1better.Race')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.CharField(default='https://i.imgur.com/xrM0pYH.png', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f1better.Track'),
        ),
        migrations.AddField(
            model_name='bet',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f1better.Driver'),
        ),
        migrations.AddField(
            model_name='bet',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f1better.Race'),
        ),
        migrations.AddField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
