from django import forms
from .models import UserProfile, HappyDay, Message


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


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['addressee', 'title', 'content']


class ResponseMSGForm(forms.ModelForm):
    parent_message = forms.ModelChoiceField(queryset=Message.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Message
        fields = ['parent_message', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent_message'].widget = forms.HiddenInput()

