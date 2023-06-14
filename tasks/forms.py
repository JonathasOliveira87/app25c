from django import forms
from .models import Task
from django_ckeditor_5.widgets import CKEditor5Widget


class TaskForm(forms.ModelForm):
    done = forms.ChoiceField(choices=Task.STATUS, initial='done', widget=forms.HiddenInput())

    class Meta:
        model = Task
        fields = ['done', 'feedback']
        widgets = {
            'done': forms.HiddenInput(),
            'description': CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }
        

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.done = 'done'
        if commit:
            instance.save()
        return instance
    

