# Generated by Django 4.2.1 on 2023-06-14 02:52

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_endtime_task_escala_task_feedback_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='task',
            name='feedback',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Texto'),
        ),
    ]