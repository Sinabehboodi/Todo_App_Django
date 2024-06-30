from django import forms

from . import models 


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ['work', 'date']



