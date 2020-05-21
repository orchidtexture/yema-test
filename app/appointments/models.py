from django.db import models

from .choices import STATUS_CHOICES

# Create your models here.

class Appointment(models.Model):
    """ A model based on a simple doctor appointment """
    pediatrician_first_name = models.CharField(
        max_length=50, 
        null=True, 
        blank=True
    )
    pediatrician_last_name = models.CharField(
        max_length=50, 
        null=True, 
        blank=True
    )
    comment = models.TextField(max_length=240, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    appointment_request = models.OneToOneField(
        "appointments.AppointmentRequest", 
        on_delete=models.CASCADE, 
        related_name='appointment'
    )
    status = models.CharField(
        max_length=3, 
        choices=STATUS_CHOICES, 
        default='REQ'
    )

    def __str__(self):
        if self.status == 'SEN':
            return (
                'Appointment for ' + self.appointment_request.first_name + ' ' 
                + self.appointment_request.last_name + ' with Doctor ' 
                + self.pediatrician_first_name + ' ' 
                + self.pediatrician_last_name + ' on '
                + str(self.date)
            )
        else:
            return (
                'Appointment for ' + self.appointment_request.first_name + ' ' 
                + self.appointment_request.last_name 
                + ' pending for assignment.'
            )


class AppointmentRequest(models.Model):
    """ A model for appointment requests performed by a patient """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.email