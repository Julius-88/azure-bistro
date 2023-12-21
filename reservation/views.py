from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation
from django.contrib import messages


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
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
