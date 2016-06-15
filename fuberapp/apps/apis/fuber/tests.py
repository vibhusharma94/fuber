from datetime import datetime
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
from .models import Cab, CabBooking


class FuberTestCase(APITestCase):
    def setUp(self):

        self.api_client = APIClient()
        self.cab = Cab.objects.create(
            driver_name="Travis Kalanick",
            number=9988, latitude=12.9668035, longitude=77.6511922)

    def test_booking_success(self):
        """
        Start Trip
        """
        payload = {"latitude": 12.9668035, "longitude": 77.6511922}
        url = reverse('start-trip', kwargs={})
        response = self.api_client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_booking_failed(self):
        """
        Start Trip Failed: origin not provided
        """
        payload = {}
        url = reverse('start-trip', kwargs={})
        response = self.api_client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_endtrip_success(self):
        """
        End Trip
        """
        booking = CabBooking.objects.create(
            cab=self.cab, start_time=datetime.now(),
            start_latitude=self.cab.latitude,
            start_longitude=self.cab.longitude)
        self.cab.is_assigned = True
        self.cab.save()
        payload = {"latitude": 12.9668035, "longitude": 77.6511922}
        url = reverse('end-trip', kwargs={"pk": booking.id})
        response = self.api_client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_endtrip_failed(self):
        """
        End Trip Failed: destination not provided
        """
        booking = CabBooking.objects.create(
            cab=self.cab, start_time=datetime.now(),
            start_latitude=self.cab.latitude,
            start_longitude=self.cab.longitude)
        self.cab.is_assigned = True
        self.cab.save()
        payload = {}
        url = reverse('end-trip', kwargs={"pk": booking.id})
        response = self.api_client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_availablecabs_success(self):
        url = reverse('cabs', kwargs={})
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bookinghistory_success(self):
        url = reverse('booking-history', kwargs={})
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
