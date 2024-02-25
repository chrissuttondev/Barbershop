from django import forms
from .models import appointment_booking

class AppointmentForm(forms.ModelForm):
    """
    Class for users to book appointemnts
    """
    class Meta:
        """
        Model and fields
        """
        model = appointment_booking
        fields = ( 'user', 'name', 'email','service', 'date', 'time', 'notes')
