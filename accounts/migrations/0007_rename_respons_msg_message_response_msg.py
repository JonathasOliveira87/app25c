# Generated by Django 4.2.1 on 2023-06-12 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_message_respons_msg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='respons_msg',
            new_name='response_msg',
        ),
    ]
