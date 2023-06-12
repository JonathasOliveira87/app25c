from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.user.username
    

class HappyDay(models.Model):
    cliente = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    data = models.DateField()

    def __str__(self):
        return f'Olá {self.cliente}, seu Happy Day foi agendado para {self.data.strftime("%d/%m/%Y")}'

    def clean(self):
        existing_agendamento = HappyDay.objects.filter(cliente=self.cliente).exists()
        if existing_agendamento and not self.pk:
            raise ValidationError('Este cliente já possui um agendamento.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Executa a validação antes de salvar o objeto
        super().save(*args, **kwargs)






class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='mensagens_enviadas', default=get_user_model())
    addressee = models.ForeignKey(get_user_model(), related_name='mensagens_recebidas', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)
    parent_message = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender} para {self.addressee.username}'
