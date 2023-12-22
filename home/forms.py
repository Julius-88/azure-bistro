from django import forms


class ConfirmDeleteForm(forms.Form):
    confirm = forms.BooleanField(label="I confirm I want to delete my account")
