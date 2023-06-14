from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Task(models.Model):
    STATUS = (('doing','Aberto'),('done' ,'Concluido'),('fail', 'Falha'))
    letra = (('all','Todas'),('a','A1'),('b','B2'),('c', 'C3'),('d', 'D4'),('e', 'E5'))
    title = models.CharField(max_length=100)
    description = CKEditor5Field('Texto', config_name='extends')
    Escala = models.CharField(max_length=10, choices=letra, default='all')
    done = models.CharField(max_length=7, choices=STATUS, default='doing')
    EndTime = models.DateField(blank=True, null=True)
    feedback = CKEditor5Field('Texto', config_name='extends', blank=True, null=True)
    created_task = models.DateTimeField(auto_now_add=True)
    updated_task = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

