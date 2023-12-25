from django.shortcuts import render, redirect, get_object_or_404
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


def confirm_delete_reservation(request, reservation_id):
    reservation = get_object_or_404(
        Reservation, id=reservation_id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Reservation successfully deleted.')
        return redirect('manage_reservation')

    return render(
        request,
        'reservation/confirm_delete_reservation.html',
        {'reservation': reservation})


def update_reservation(request, reservation_id):
    reservation = get_object_or_404(
        Reservation,
        id=reservation_id,
        user=request.user)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation has been updated.')
            return redirect('manage_reservation')
    else:
        form = ReservationForm(instance=reservation)

    return render(
        request,
        'reservation/update_reservation.html',
        {'form': form, 'reservation_id': reservation_id})


def all_reservations(request):
    reservations = Reservation.objects.all().order_by(
        '-reservation_date', '-reservation_time')
    return render(
        request,
        'reservation/all_reservations.html', {'reservations': reservations})


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
