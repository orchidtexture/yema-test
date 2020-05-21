from rest_framework import serializers

from appointments.models import AppointmentRequest


class AppointmentRequestSerializer(serializers.ModelSerializer):
    """ 
    Serializer that provides the fields needed for an appointment request 
    creation
    """
    
    class Meta:
        model = AppointmentRequest
        fields = (
            'first_name',
            'last_name',
            'email',
        )