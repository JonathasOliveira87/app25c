# Generated by Django 4.2.1 on 2023-06-14 00:37

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('send_date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('addressee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_recebidas', to=settings.AUTH_USER_MODEL)),
                ('parent_message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='accounts.message')),
                ('sender', models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.PROTECT, related_name='mensagens_enviadas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Mensagem',
        ),
    ]