from django import forms
from .models import BoxItem


class AddBoxItemForm(forms.ModelForm):
    class Meta:
        model: BoxItem
        fields: "__all__"
