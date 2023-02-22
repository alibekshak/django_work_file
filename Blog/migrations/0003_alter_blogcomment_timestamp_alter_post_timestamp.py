# Generated by Django 4.1.7 on 2023-02-22 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_blogcomment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='timeStamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 12, 42, 30, 474822, tzinfo=datetime.timezone.utc), verbose_name='Дата коммента'),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 18, 42, 30, 474307), verbose_name='Дата публикации'),
        ),
    ]