from django.urls import path

from appointments.api_v1 import endpoints

urlpatterns = [
    path(
        route='appointments/request/',
        view=endpoints.AppointmentRequestEndpoint.as_view(),
        name='appointment_request'
    ),
]