from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


TIME_CHOICES = [
    ('18:00', '18:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'),
    ('22:00', '22:00'),
]


class Reservation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    number_of_people = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(4)
        ]
    )
    reservation_date = models.DateField()
    reservation_time = models.TimeField(choices=TIME_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f'Reservation for {self.number_of_people} people on '
            f'{self.reservation_date} at {self.reservation_time} '
            f'by {self.user.username}'
        )
