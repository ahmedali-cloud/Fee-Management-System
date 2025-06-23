
# from django.contrib import admin
# from .models import Fee
# from django import forms

# class FeeForm(forms.ModelForm):
#     student = forms.CharField()  # override ForeignKey with CharField

#     class Meta:
#         model = Fee
#         fields = '__all__'

# class FeeAdmin(admin.ModelAdmin):
#     form = FeeForm

# admin.site.register(Fee, FeeAdmin)

# fees/admin.py

from django.contrib import admin
from .models import Fee
from .forms import FeeForm

class FeeAdmin(admin.ModelAdmin):
    form = FeeForm
    autocomplete_fields = ['student']  # Allows typing GR number
    list_display = ['student', 'fee_month', 'amount', 'paid_amount']

admin.site.register(Fee, FeeAdmin)
