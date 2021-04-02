from django import forms

class PinChangeForm(forms.Form):
    pin = forms.IntegerField(max_value=40, help_text='max pin is 40')