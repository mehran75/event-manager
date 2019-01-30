from django.forms import ModelForm
from database.models import Event
from django import forms


class EventForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Event
        fields = ['title', 'body', 'picture', 'is_active', 'category']
