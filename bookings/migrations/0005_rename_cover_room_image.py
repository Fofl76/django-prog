# Generated by Django 5.0.6 on 2024-06-15 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_room_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='cover',
            new_name='image',
        ),
    ]
