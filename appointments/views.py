from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from allauth.account.views import LoginView
from .forms import AppointmentForm
from .models import appointment_booking

# view to redirect user to appointments.html after sign up success

# class signin_success(SignupView):
def get_success_url(self):
    return reverse_lazy('appointments') 


# Create your views here.
def appointments(request):
    appointments = appointment_booking.objects.all()
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
            print(messages.get_messages(request))
    
            return redirect('appointments')
    else:
        appointment_form = AppointmentForm()   
        return render(
            request,
            "appointments/appointments.html",
            {'appointment_form': appointment_form}
        )


def appointment_edit(request, appointment_id):
    appointment = get_object_or_404(appointment_booking, pk=appointment_id)
    if request.method == "POST":
        if appointment.user == request.user.id:
            appointment_form = AppointmentForm(data=request.POST, instance=appointment)
            if appointment_form.is_valid():
                appointment_form.save()
                messages.success('Appointment Updated')
                return redirect('appointments')
            else:
                messages.error('Error updating appointment!')
    else:
       
        if request.user.is_authenticated and appointment.user == request.user:
            appointment_form = AppointmentForm(instance=appointment)
            return render(
                        request, 
                        "appointments/appointments_edit.html", 
                        {'appointment_form': appointment_form})
        else:
            return HttpResponse(
                                "Not authorized to edit this appointment!", 
                                status=403)
