# Generated by Django 4.0.1 on 2022-01-14 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False, verbose_name='상태'),
        ),
    ]