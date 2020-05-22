from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string

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
        if self.status == 'SNT':
            return (
                'Cita de ' + self.appointment_request.first_name + ' ' 
                + self.appointment_request.last_name + ' con el Doctor ' 
                + self.pediatrician_first_name + ' ' 
                + self.pediatrician_last_name + ' el '
                + str(self.date) #TODO: make date and time human readable
            )
        else:
            return (
                'Cita para ' + self.appointment_request.first_name + ' ' 
                + self.appointment_request.last_name 
                + ' pendiente de asignación.'
            )
    
    @property
    def is_completed(self):
        """
        Property that returns true if all fields of the instance are populated
        or returns a list of non-populated fields
        """
        fields_to_complete = []
        if self.pediatrician_first_name is None:
            fields_to_complete.append('Nombre del pediatra')
        if self.pediatrician_last_name is None:
            fields_to_complete.append('Apellido del pediatra')
        if self.date is None:
            fields_to_complete.append('Fecha de la consulta')
        if len(fields_to_complete) > 0:
            return fields_to_complete
        else:
            return True

    def send_appointment_email(self):
        """
        Method to send an email with the appointment information to the patient
        """
        date = self.date.date()
        time = self.date.time()
        doctor_name = (
            self.pediatrician_first_name + ' ' 
            + self.pediatrician_last_name
        )
        context = {
            'name': self.appointment_request.first_name,
            'date': date,
            'time': time,
            'doctor_name': doctor_name,
            'comment': self.comment
        }
        msg_plain = render_to_string('email.txt', context)
        msg_html = render_to_string('email.html', context)
        send_mail(
            'Tu cita con el pediatra',
            msg_plain,
            'luisdaniel.guzmanp+sendgrid@gmail.com',
            [self.appointment_request.email],
            html_message=msg_html,
        )



class AppointmentRequest(models.Model):
    """ A model for appointment requests performed by a patient """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.email

@receiver(post_save, sender=AppointmentRequest)
def create_appointment(sender, instance, **kwargs):
    """ 
    Django signal that creates an Appointment instance after the AppointmentRequest is created
    """
    if instance.appointment is None:
        Appointment.objects.create(**{'appointment_request': instance})