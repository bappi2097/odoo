from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'
        widgets = {
            'mod_date': forms.DateInput(attrs={'type': 'date'}),
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
        }