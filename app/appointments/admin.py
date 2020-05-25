from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import Appointment, AppointmentRequest

# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    change_form_template = "admin/change_form.html"

    def response_change(self, request, obj):
        if "_send-email" in request.POST:
            if obj.is_completed == True:
                #TODO: Send email
                obj.send_appointment_email()
                obj.status = 'SNT'
                obj.save()
                self.message_user(request, "Se ha enviado un email a " + obj.appointment_request.first_name)
            else:
                missing_fields = ', '.join(obj.is_completed)
                self.message_user(request, "Por favor completa los campos siguientes: " + missing_fields)
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)


@admin.register(AppointmentRequest)
class AppointmentRequestAdmin(admin.ModelAdmin):
     def has_add_permission(self, request, obj=None):
        return False