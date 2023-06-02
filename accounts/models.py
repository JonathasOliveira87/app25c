from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.user.username
    

from django.core.exceptions import ValidationError

class HappyDay(models.Model):
    cliente = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    data = models.DateField()

    def __str__(self):
        return f'Agendamento para {self.cliente} em {self.data}'

    def clean(self):
        existing_agendamento = HappyDay.objects.filter(cliente=self.cliente).exists()
        if existing_agendamento and not self.pk:
            raise ValidationError('Este cliente já possui um agendamento.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Executa a validação antes de salvar o objeto
        super().save(*args, **kwargs)
