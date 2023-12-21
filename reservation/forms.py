from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = [
            'reservation_date',
            'reservation_time',
            'number_of_guests'
        ]
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'})
        }
