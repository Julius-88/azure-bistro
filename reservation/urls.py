from django.urls import path
from . import views

urlpatterns = [
    path('reservation/', views.reservation, name='reservation'),
    path(
        'manage_reservation/',
        views.manage_reservation,
        name='manage_reservation'),
    path(
        'confirm_delete_reservation/<int:reservation_id>/',
        views.confirm_delete_reservation,
        name='confirm_delete_reservation'),
    path(
        'update_reservation/<int:reservation_id>/',
        views.update_reservation,
        name='update_reservation'),
    path('all_reservations', views.all_reservations, name='all_reservations'),
    path(
        'admin_update_reservation.html/<int:reservation_id>/',
        views.admin_update_reservation,
        name='admin_update_reservation'),
    path(
        'admin_delete_reservation.html/<int:reservation_id>/',
        views.admin_delete_reservation,
        name='admin_delete_reservation'),
]
