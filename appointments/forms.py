from datetime import date, timedelta
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
        exclude = ['user']
        presentday = date.today()
        tomorrow = presentday + timedelta(1)
        widgets = {
            'date': forms.DateInput(
                attrs={
                        'type': 'date',
                        'min': tomorrow,
                        'class': 'form-control'
                        }
            )
        }
