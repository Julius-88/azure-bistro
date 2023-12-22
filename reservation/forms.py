from django import forms
from .models import Reservation, TIME_CHOICES


class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        reservation_date = kwargs.pop('reservation_date', None)
        super().__init__(*args, **kwargs)
        if reservation_date:
            booked_times = Reservation.objects.filter(
                reservation_date=reservation_date).values_list(
                    'reservation_time', flat=True)
            available_times = [
                time for time in TIME_CHOICES if time not in booked_times]
            self.fields['reservation_time'].choices = available_times

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
