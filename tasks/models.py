from django.db import models

class Task(models.Model):
    STATUS = (('doing','Aberto'),('done' ,'Concluido'),('fail', 'Falha'))
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.CharField(max_length=7, choices=STATUS,)
    EndTime = models.DateField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    created_task = models.DateTimeField(auto_now_add=True)
    updated_task = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title


