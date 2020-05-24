from django.test import TestCase

from rest_framework.test import APIClient

from appointments.models import AppointmentRequest, Appointment


class AppointmentRequestTest(TestCase):
    """ Tests for AppointmentRequest endpoint """
    def setUp(self):
        self.default_data = {
            'first_name': 'Test',
            'last_name': 'Name',
            'email': 'test@email.com'
        }

    def test_appointment_create(self):
        """ 
        Tests if appointment request endpoint creates an appointment request 
        instance and a related appointment
        """
        client = APIClient()
        response = client.post(
            'http://localhost:8000/api/v1/appointments/request/',
            data=self.default_data,
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(AppointmentRequest.objects.all().count(), 1)
        self.assertEqual(Appointment.objects.all().count(), 1)