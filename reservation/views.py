from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation
from django.contrib import messages
import datetime


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            try:
                reservation_date = datetime.datetime.strptime(request.POST.get(
                    'reservation_date'), '%Y-%m-%d').date()
            except (TypeError, ValueError):
                messages.error(
                    request, "Invalid date. Please select a valid date.")
                return render(
                    request, 'reservation/reservation.html', {'form': form})

            reservation_time = form.cleaned_data['reservation_time']

            # Check if the time slot is already booked
            if Reservation.objects.filter(
                    reservation_date=reservation_date,
                    reservation_time=reservation_time).exists():
                messages.error(request, "This time slot is already booked.")
                return render(
                    request, 'reservation/reservation.html', {'form': form})

            # Save the new reservation
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.reservation_date = reservation_date
            reservation.save()
            messages.success(request, 'Reservation made successfully!')
            return redirect('home')
    else:
        form = ReservationForm()
    return render(request, 'reservation/reservation.html', {'form': form})


def manage_reservation(request):
    user_reservations = Reservation.objects.filter(user=request.user).order_by(
        '-created_at')
    return render(
        request,
        'reservation/manage_reservation.html',
        {'reservations': user_reservations})


"""
These resources have been used in order to create the above code.
https://docs.djangoproject.com/en/5.0/topics/forms/
https://docs.djangoproject.com/en/5.0/ref/forms/widgets/
https://docs.djangoproject.com/en/5.0/ref/forms/validation/
https://docs.djangoproject.com/en/5.0/topics/db/models/
https://docs.djangoproject.com/en/5.0/topics/db/queries/
https://docs.python.org/3/library/datetime.html
https://docs.djangoproject.com/en/5.0/ref/contrib/messages/
https://www.youtube.com/watch?v=s5xbtuo9pR0&t=102s
Code Institute: I think therefore I blog, Hello Django

"""
