from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from allauth.account.views import LoginView
from .forms import AppointmentForm

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
            appointment = appointment_form.save(commit=False)
            appointment.user = request.user
            print(request.user)
            appointment_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Appointment made')
            print(messages.add_message.SUCCESS)
            return redirect('appointments')
    else:
        appointment_form = AppointmentForm()  

        
        return render(
            request,
            "appointments/appointments.html",
            {'appointment_form': appointment_form}
            )    

