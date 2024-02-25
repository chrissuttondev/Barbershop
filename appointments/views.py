from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import AppointmentForm

# Create your views here.
def appointments(request):
    return render(
        request,
        "appointments/appointments.html"
        )

    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST) 
        print(appointment_form)
        if appointment_form.is_valid():
            appointment_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Appointment made')
    else:
        appointment_form =AppointmentForm()        

    
        return render(
            request,
            "appointments/appointments.html",
            {'appointment_form': appointment_form}
            )    

