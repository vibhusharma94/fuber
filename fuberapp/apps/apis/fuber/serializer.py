from rest_framework import serializers
from rest_framework import exceptions
from .models import Cab, CabBooking


class CabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab


class BookingSerializer(serializers.ModelSerializer):
    cab = CabSerializer()

    class Meta:
        model = CabBooking


class TripStartRequestSerializer(serializers.Serializer):
    color = serializers.CharField(required=False)
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)


class TripEndRequestSerializer(serializers.Serializer):
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)
