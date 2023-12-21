from django.urls import path
from . import views

urlpatterns = [
    path('reservation/', views.reservation, name='reservation'),
    path(
        'manage_reservation/',
        views.manage_reservation,
        name='manage_reservation'),
]
