from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
import math


class Cab(models.Model):

    BLACK = "black"
    WHITE = "white"
    PINK = "pink"
    COLOR_CHOICES = (
        (BLACK, 'black'),
        (WHITE, 'white'),
        (PINK, 'pink'),
    )

    FUBERGO = "fuberGo"
    FUBERX = "fuberX"
    FUBERXL = "fuberXL"
    CAR_CHOICES = (
        (FUBERGO, 'fuberGo'),
        (FUBERX, 'fuberX'),
        (FUBERXL, 'fuberXL'),
    )
    driver_name = models.CharField(max_length=255)
    number = models.PositiveIntegerField(_("Cab Number"), unique=True)
    cab_type = models.CharField(
        _("Cab Type"), max_length=30, choices=CAR_CHOICES, default=FUBERGO)
    color = models.CharField(
        _('Cab Color'), max_length=10, choices=COLOR_CHOICES, default=BLACK)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_assigned = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created'
        db_table = "cab"

    def __unicode__(self):
        return "%s %s" % (self.cab_type, self.number)

    def color_is_pink(self):
        if self.color == self.PINK:
            return True
        return False

    def start_trip(self):  # start trip
        booking = CabBooking.objects.create(
            cab=self, start_time=datetime.now(),
            start_latitude=self.latitude,
            start_longitude=self.longitude)
        self.is_assigned = True
        self.save()
        return booking


class CabBooking(models.Model):
    CHARGE_PER_MINUTE = 1
    CHARGE_PER_KILOMETER = 2
    PINK_CAB_CHARGE = 5
    BASE_CHARGE = 0
    cab = models.ForeignKey(Cab, related_name='bookings')
    fare = models.PositiveIntegerField(_("Cab Fare"), default=BASE_CHARGE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    start_latitude = models.FloatField()
    start_longitude = models.FloatField()
    end_latitude = models.FloatField(null=True, blank=True)
    end_longitude = models.FloatField(null=True, blank=True)
    is_running = models.BooleanField(default=True)

    class Meta:
        get_latest_by = 'created'
        db_table = "cab_booking"

    def __unicode__(self):
        return self.cab.driver_name

    def end_trip(self, latitude, longitude):  # end trip
        self.end_time = datetime.now()
        self.end_latitude = latitude
        self.end_longitude = longitude
        self.save()
        cab = self.cab
        cab.is_assigned = False
        cab.latitude = latitude
        cab.longitude = longitude
        cab.save()
        self.calculate_fare()

    def calculate_fare(self):  # calculate fare trip fare
        # if trip is active
        if self.is_running and self.fare == 0:
            origin = self.start_latitude, self.start_longitude
            destination = self.end_latitude, self.end_longitude
            distance = self.calculate_distance(origin, destination)
            distance_charge = distance * self.CHARGE_PER_KILOMETER

            minutes = self.calculate_trip_minute()
            minute_charge = minutes * self.CHARGE_PER_MINUTE

            total_charge = distance_charge + minute_charge
            if self.cab.color_is_pink:  # if cab color is pink then extra 5 dogecoin.
                total_charge += self.PINK_CAB_CHARGE

            self.fare = total_charge
            self.is_running = False
            self.save()

    def calculate_distance(self, origin, destination):  # calculate trip distance in km
        lat1, lon1 = origin
        lat2, lon2 = destination
        radius = 6371  # km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c

        return d

    def calculate_trip_minute(self):  # calculate trip time in minutes
        trip_time = self.end_time - self.start_time
        minutes, seconds = divmod(trip_time.days * 86400 + trip_time.seconds, 60)
        return minutes
