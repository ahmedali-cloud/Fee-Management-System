# fees/forms.py

from django import forms
from .models import Fee

class FeeForm(forms.ModelForm):
    fee_month = forms.DateField(
        widget=forms.TextInput(attrs={'placeholder': 'e.g. April 2025'}),
        label='Fee Month (e.g. April 2025)'
    )

    class Meta:
        model = Fee
        fields = '__all__'
