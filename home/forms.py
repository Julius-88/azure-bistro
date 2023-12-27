from django import forms


class ConfirmDeleteForm(forms.Form):
    # Form for confirming account deletion with a single checkbox
    confirm = forms.BooleanField(label="I confirm I want to delete my account")
