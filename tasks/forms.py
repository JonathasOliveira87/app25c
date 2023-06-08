from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    done = forms.ChoiceField(choices=Task.STATUS, initial='done', widget=forms.HiddenInput())

    class Meta:
        model = Task
        fields = ['done', 'feedback']
        widgets = {
            'done': forms.HiddenInput(),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.done = 'done'
        if commit:
            instance.save()
        return instance
    

