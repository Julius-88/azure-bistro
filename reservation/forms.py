from django import forms
from .models import Reservation, TIME_CHOICES


class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        reservation_date = kwargs.pop('reservation_date', None)
        reservation_instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)

        if reservation_date:
            booked_times_query = Reservation.objects.filter(
                reservation_date=reservation_date)
            if reservation_instance:
                booked_times_query = booked_times_query.exclude(
                    id=reservation_instance.id)
            booked_times = booked_times_query.values_list(
                'reservation_time', flat=True)

            available_times = [
                time for time in TIME_CHOICES if time[0] not in booked_times
            ]

            if reservation_instance and (
                reservation_instance.reservation_time,
                    reservation_instance.get_reservation_time_display(

                    )) not in available_times:
                available_times.append((
                    reservation_instance.reservation_time,
                    reservation_instance.get_reservation_time_display()))

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
