from django import forms
from .models import UserProfile, HappyDay

class UserProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(label='Profile picture')  # Usar o mesmo nome do campo no modelo

    class Meta:
        model = UserProfile
        fields = ['profile_pic']  # Usar o mesmo nome do campo no modelo


class HappyDayForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha para confirmar o agendamento'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Selecione a data do agendamento'}))

    class Meta:
        model = HappyDay
        fields = ['password', 'date']
