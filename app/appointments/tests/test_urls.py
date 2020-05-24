from django.test import TestCase, Client
from django.urls import reverse


class UrlsTests(TestCase):
    """ Tests for appointments urls """

    def setUp(self):
        self.client = Client()

        self.default_data = {
            'first_name': 'Test',
            'last_name': 'Name',
            'email': 'test@email.com'
        }

        self.default_wrong_data = {
            'last_name': 'Name',
            'email': 'test@email.com'
        }
    
    def test_appointment_request(self):
        """ Tests the appointment_request url """
        url = reverse('api_v1_appointments:appointment_request')
        response = self.client.post(url, self.default_data)
        self.assertEqual(response.status_code, 201)

    def test_appointment_request_wrong_data(self):
        """ Tests the appointment_request url with wrong data"""
        url = reverse('api_v1_appointments:appointment_request')
        response = self.client.post(url, self.default_wrong_data)
        self.assertEqual(response.status_code, 400)
