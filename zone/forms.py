from django import forms
from .models import Zone


class ZoneCreateForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ('name',)
