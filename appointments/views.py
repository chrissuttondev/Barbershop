from django.shortcuts import render
from django.http import HttpResponse
from .forms import AppointmentForm

# Create your views here.
def appointments(request):
    return render(
        request,
        "appointments/appointments.html"
        )

    if 

    booking_form =BookingForm()
    
    return render(
        request,
        "appointments/appointments.html",
        {'booking_form': booking_form}
        )    

