from django.shortcuts import render, redirect
from .forms import ConfirmDeleteForm


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def menu(request):
    """ A view to return the menu page """
    return render(request, 'home/menu.html')


def contact(request):
    """ A view to return the contact page """
    return render(request, 'home/contact.html')


def confirm_delete_account(request):
    """ A view to return the confirm delete account page """
    if request.method == 'POST':
        form = ConfirmDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            request.user.delete()
            return redirect('home')
    else:
        form = ConfirmDeleteForm()

    return render(request, 'home/confirm_delete_account.html', {'form': form})
