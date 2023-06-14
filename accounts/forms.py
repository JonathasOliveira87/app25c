from django import forms
from .models import UserProfile, HappyDay, Message
from django_ckeditor_5.widgets import CKEditor5Widget


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False

    class Meta:
        model = Message
        fields = ['addressee', 'title', 'content']
        widgets = {
              "content": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }
        

class ResponseMSGForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False

    class Meta:
        model = Message
        fields = ['content']
        widgets = {
              "content": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }
        






