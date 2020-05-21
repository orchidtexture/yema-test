from django.contrib import admin

from .models import Appointment, AppointmentRequest

# Register your models here.

admin.site.register(AppointmentRequest)
admin.site.register(Appointment)