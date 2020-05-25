from rest_framework import generics

from appointments.models import AppointmentRequest, Appointment
from .serializers import AppointmentRequestSerializer

class AppointmentRequestEndpoint(generics.CreateAPIView):
    """ Endpoint responsible for creating a new appointment request """
    queryset = AppointmentRequest.objects.all()
    serializer_class = AppointmentRequestSerializer

    def perform_create(self, serializer):
        """ creates a related appointment object """
        appointment_request = serializer.save()
        Appointment.objects.create(**{
                'appointment_request': appointment_request
        })