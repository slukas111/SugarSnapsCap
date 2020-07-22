
from django import forms
from .models import BoxItem
from tempus_dominus.widgets import DateTimePicker


class AddBoxItemForm(forms.ModelForm):
    time_field = forms.TimeField(
        widget=DateTimePicker(
            options={
                'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
                'defaultDate': '1970-01-01T14:56:00'
            },
            attrs={
                'input_toggle': True,
                'input_group': False,
            },
        ),
    )
    datetime_field = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )
    class Meta:
        model: BoxItem
        fields: "__all__"
