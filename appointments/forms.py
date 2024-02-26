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
        exclude = [ 'email', 'user']
        widgets = {
            'student_date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'placeholder': datetoday(), 'class': 'form-control'}
            )
        }
