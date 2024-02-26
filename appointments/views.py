from allauth.account.views import SignupView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import AppointmentForm

# https://stackoverflow.com/questions/60404987/how-can-i-overide-django-allauth-signup-success-url

# view to redirect user to appointments.html after sign up success

# class signin_success(SignupView):
def get_success_url(self):
    return reverse_lazy('appointments') 



# Create your views here.
def appointments(request):
   
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST) 
        print(appointment_form)
        if appointment_form.is_valid():
            appointment_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Appointment made')
    else:
        appointment_form = AppointmentForm()  

        
        return render(
            request,
            "appointments/appointments.html",
            {'appointment_form': appointment_form}
            )    

