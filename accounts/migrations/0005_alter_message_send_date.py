# Generated by Django 4.2.1 on 2023-06-12 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_message_send_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='send_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]