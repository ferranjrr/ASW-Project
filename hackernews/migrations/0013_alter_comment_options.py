# Generated by Django 4.0.3 on 2022-04-16 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackernews', '0012_comment_level_comment_lft_comment_rght_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-posted_at_date', '-posted_at_time')},
        ),
    ]
