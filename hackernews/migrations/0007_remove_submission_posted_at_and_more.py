# Generated by Django 4.0.3 on 2022-04-06 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hackernews', '0006_remove_user_created_at_user_created_at_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='posted_at',
        ),
        migrations.AddField(
            model_name='submission',
            name='posted_at_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='submission',
            name='posted_at_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
