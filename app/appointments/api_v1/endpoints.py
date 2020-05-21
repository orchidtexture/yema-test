from rest_framework import generics

from appointments.models import AppointmentRequest
from .serializers import AppointmentRequestSerializer

class AppointmentRequestEndpoint(generics.CreateAPIView):
    """ Endpoint responsible for creating a new appointment request """
    queryset = AppointmentRequest.objects.all()
    serializer_class = AppointmentRequestSerializer