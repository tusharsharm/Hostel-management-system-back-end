# Generated by Django 4.2.6 on 2024-03-18 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0036_remove_room_registrationnumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_Room',
            field=models.BooleanField(default=False),
        ),
    ]
