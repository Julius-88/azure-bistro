from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Reservation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import datetime


@login_required
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


@login_required
def manage_reservation(request):
    user_reservations = Reservation.objects.filter(user=request.user).order_by(
        '-created_at')
    return render(
        request,
        'reservation/manage_reservation.html',
        {'reservations': user_reservations})


@login_required
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


@login_required
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

# Admin Section


@login_required
@staff_member_required
def all_reservations(request):
    reservations = Reservation.objects.all().order_by(
        '-reservation_date', '-reservation_time')
    return render(
        request,
        'reservation/all_reservations.html', {'reservations': reservations})


@login_required
@staff_member_required
def admin_update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation updated successfully!')
            return redirect('all_reservations')
    else:
        form = ReservationForm(instance=reservation)

    return render(
        request, 'reservation/admin_update_reservation.html', {'form': form})


@login_required
@staff_member_required
def admin_delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Reservation successfully deleted!')
        return redirect('all_reservations')

    return render(
        request,
        'reservation/admin_delete_reservation.html',
        {'reservation': reservation})
