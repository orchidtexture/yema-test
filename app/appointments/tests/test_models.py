from datetime import datetime

from django.test import TestCase
from django.core import mail

from appointments.models import Appointment, AppointmentRequest

class AppointmentTestCase(TestCase):
    """ Tests for Appointment model """
    def setUp(self):
        self.appointment_request = AppointmentRequest.objects.create(
            first_name = 'Test',
            last_name = 'User',
            email = 'test@email.com'
        )

        self.appointment = Appointment.objects.create(
            appointment_request = self.appointment_request,
        )

        self.default_data = {
            'pediatrician_first_name': 'first name',
            'pediatrician_last_name': 'last_name',
            'date': datetime.now()
        }

    def test_appointment_is_not_completed(self):
        """ 
        tests if there are missing fields to populate an appointment instance 
        """
        self.assertIsNot(self.appointment.is_completed, True)

    def test_appointment_is_completed(self):
        """ 
        tests if an appointment instance's fields are completely populated 
        """
        self.appointment.pediatrician_first_name = self.default_data['pediatrician_first_name']
        self.appointment.pediatrician_last_name = self.default_data['pediatrician_last_name']
        self.appointment.date = self.default_data['date']
        self.assertTrue(self.appointment.is_completed)

    def test_send_appointment_email(self):
        """ 
        tests if an email with the appointment is sent and its subject
        """
        self.appointment.pediatrician_first_name = self.default_data['pediatrician_first_name']
        self.appointment.pediatrician_last_name = self.default_data['pediatrician_last_name']
        self.appointment.date = self.default_data['date']
        self.appointment.send_appointment_email()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Tu cita con el pediatra')