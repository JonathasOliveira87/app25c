# Generated by Django 4.2.1 on 2023-06-14 00:37

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='EndTime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='Escala',
            field=models.CharField(choices=[('all', 'Todas'), ('a', 'A1'), ('b', 'B2'), ('c', 'C3'), ('d', 'D4'), ('e', 'E5')], default='all', max_length=10),
        ),
        migrations.AddField(
            model_name='task',
            name='feedback',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.CharField(choices=[('doing', 'Aberto'), ('done', 'Concluido'), ('fail', 'Falha')], default='doing', max_length=7),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]