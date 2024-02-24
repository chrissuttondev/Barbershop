from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#Service Constant
SERVICE_OPTIONS = (
    (0, "Cut and finish"),
    (1, "Short back and sides"),
    (2, "Skinhead"),
    (3, "Skin fade"),
    (4, "Afro hair cut"),
    (5, "Beard trim"),
    (6, "Cut, finish and beard trim"),
    (7, "Short back and sides and beard trim"),
    (8, "Skinhead and beard trim"),
    (9, "Skin fade and beard trim"),
    (10, "Afro hair cut and beard trim")

)

#Time Slot Constant
TIME_SLOTS = (
    ("09:00", "09:00"),
    ("09:30", "09:30"),
    ("10:00", "10:00"),
    ("10:30", "10:30"),
    ("11:00", "11:00"),
    ("11:30", "11:30"),
    ("12:00", "12:00"),
    ("12:30", "12:30"),
    ("13:00", "13:00"),
    ("13:30", "13:30"),
    ("14:00", "14:00"),
    ("14:30", "14:30"),
    ("15:00", "15:00"),
    ("15:30", "15:30"),
    ("16:00", "16:00"),
    ("16:30", "16:30"),
)

# Create your models here.
class appointment_booking(models.Model):
    """
    Stores customer appointment bookings
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    service = models.IntegerField(choices=SERVICE_OPTIONS, default=0)
    date = models.DateField(default=timezone.now)
    time = models.CharField(choices=TIME_SLOTS, default="09:00")
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user} | {self.name} | {self.email} | {self.service} | {self.time} | {self.notes}"