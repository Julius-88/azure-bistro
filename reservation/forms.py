from django import forms
from .models import Reservation, TIME_CHOICES


class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """
        Extract reservation_date from kwargs
        and remove it to prevent issues with super().__init__()
        """
        reservation_date = kwargs.pop('reservation_date', None)
        reservation_instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)

        # Checks available reservation times based on the provided date
        if reservation_date:
            # Query to find all reservations on the given date
            booked_times_query = Reservation.objects.filter(
                reservation_date=reservation_date)
            # Exclude the current instance from the query if it exists
            if reservation_instance:
                booked_times_query = booked_times_query.exclude(
                    id=reservation_instance.id)
            # List of times that are already booked
            booked_times = booked_times_query.values_list(
                'reservation_time', flat=True)
            # Filter out the booked times from the available choices
            available_times = [
                time for time in TIME_CHOICES if time[0] not in booked_times
            ]
            # If updating a reservation, ensure the current time is available
            if reservation_instance and (
                reservation_instance.reservation_time,
                    reservation_instance.get_reservation_time_display(
                    )) not in available_times:
                available_times.append((
                    reservation_instance.reservation_time,
                    reservation_instance.get_reservation_time_display()))
            # Set the filtered choices to the reservation_time field
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
