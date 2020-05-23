from rest_framework import generics

from appointments.models import AppointmentRequest, Appointment
from .serializers import AppointmentRequestSerializer

class AppointmentRequestEndpoint(generics.CreateAPIView):
    """ Endpoint responsible for creating a new appointment request """
    queryset = AppointmentRequest.objects.all()
    serializer_class = AppointmentRequestSerializer

    def create(self, request, *args, **kwargs):
        """ I wanted to do some stuff with serializer.data here """
        Appointment.objects.create(**{'appointment_request': self})

        return super(MemberCreate, self).create(request, *args, **kwargs)