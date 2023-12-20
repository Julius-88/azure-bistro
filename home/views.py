from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def menu(request):
    """ A view to return the menu page """
    return render(request, 'home/menu.html')


def contact(request):
    """ A view to return the contact page """
    return render(request, 'home/contact.html')
