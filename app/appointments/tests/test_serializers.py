from django.test import TestCase

from appointments.models import AppointmentRequest
from appointments.api_v1.serializers import AppointmentRequestSerializer


class AppointmentRequestSerializerTests(TestCase):
    """ Tests for the AppointmentRequestSerializer """

    def setUp(self):
        self.attributes = {
            'first_name': 'Test',
            'last_name': 'Name',
            'email': 'test@email.com',
        }

        self.serializer_data = {
            'first_name': 'Test2',
            'last_name': 'Name2',
            'email': 'test2@email.com',
        }

        self.appointment_request = AppointmentRequest.objects.create(
            **self.attributes
        )
        self.serializer = AppointmentRequestSerializer(
            instance=self.appointment_request
        )
    
    def test_contains_expected_fields(self):
        """ Tests if the serializer contains the expected fields """
        data = self.serializer.data

        self.assertCountEqual(
            data.keys(), ['first_name', 'last_name', 'email']
        )
    
    def test_first_name_field_content(self):
        """ 
        Check if the serializers produces the expected data for first_name 
        """
        data = self.serializer.data

        self.assertEqual(data['first_name'], self.attributes['first_name'])
    
    def test_last_name_field_content(self):
        """ 
        Check if the serializers produces the expected data for last_name 
        """
        data = self.serializer.data

        self.assertEqual(data['last_name'], self.attributes['last_name'])

    def test_email_field_content(self):
        """ 
        Check if the serializers produces the expected data for email 
        """
        data = self.serializer.data

        self.assertEqual(data['email'], self.attributes['email'])