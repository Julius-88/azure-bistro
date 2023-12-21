from django.shortcuts import render, redirect
from .forms import ReservationForm


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('home')
    else:
        form = ReservationForm()

    return render(request, 'reservation/reservation.html', {'form': form})
