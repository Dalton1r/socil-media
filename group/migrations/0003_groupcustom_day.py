# Generated by Django 4.0.6 on 2022-08-01 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_post_likemodel_comment_bookmarkmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupcustom',
            name='day',
            field=models.DateTimeField(default=datetime.timezone),
        ),
    ]