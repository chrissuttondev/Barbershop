from django.urls import path
from . import views as appointment_views


urlpatterns = [
    path('', appointment_views.appointments, name='appointments')

]