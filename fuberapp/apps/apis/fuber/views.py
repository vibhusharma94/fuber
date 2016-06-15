# rest framework modules
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.authentication import SessionAuthentication

# app level modules
from .serializer import (
    CabSerializer,
    BookingSerializer,
    TripStartRequestSerializer,
    TripEndRequestSerializer)
from .models import Cab, CabBooking


# No need for csrf verification
class UnsafeSessionAuthentication(SessionAuthentication):

    def authenticate(self, request):
        # Get the underlying HttpRequest object
        request = request._request
        user = getattr(request, 'user', None)

        # Unauthenticated, CSRF validation not required
        if not user or not user.is_active:
            return None
        return (user, None)


class StartTripApi(generics.GenericAPIView):

    queryset = Cab.objects.filter(is_assigned=False)
    authentication_classes = (UnsafeSessionAuthentication,)

    def post(self, request):
        data = request.data.copy()
        serializer = TripStartRequestSerializer(data=data)
        if serializer.is_valid():
            startlat = serializer.validated_data["latitude"]
            startlng = serializer.validated_data["longitude"]
            color = serializer.validated_data.get("color")
            if color:
                sql_color = " AND color='%s' " % color
            else:
                sql_color = ""

            sql_prefix = """
                SELECT id, number, cab_type, color, is_assigned, latitude, longitude,
                SQRT(
                POW(69.1 * (latitude - %s), 2) +
                POW(69.1 * (%s - longitude) * COS(latitude / 57.3), 2)) AS distance
                FROM cab  WHERE is_assigned = 0
            """
            sql_suffix = "ORDER BY distance LIMIT 1;"
            query = sql_prefix + sql_color + sql_suffix
            query = query % (startlat, startlng)
            print query
            cabs = Cab.objects.raw(query)
            cabs = list(cabs)
            try:
                cab = cabs[0]
                print cab
            except IndexError:
                cab = None
            if not cab:
                response_data = {"trip": None}
            else:
                booking = cab.start_trip()
                response_data = {"trip": BookingSerializer(instance=booking).data}
            return Response(response_data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EndTripApi(generics.GenericAPIView):

    queryset = CabBooking.objects.filter(is_running=True)
    authentication_classes = (UnsafeSessionAuthentication,)

    def post(self, request, pk):
        booking = self.get_object()
        data = request.data.copy()
        serializer = TripEndRequestSerializer(data=data)
        if serializer.is_valid():
            endlat = serializer.validated_data["latitude"]
            endlng = serializer.validated_data["longitude"]
            booking.end_trip(endlat, endlng)
            response_data = BookingSerializer(instance=booking).data
            return Response(response_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CabsApi(generics.ListAPIView):

    queryset = Cab.objects.filter(is_assigned=False)
    serializer_class = CabSerializer
    authentication_classes = (UnsafeSessionAuthentication,)


class BookingHistoryApi(generics.ListAPIView):

    queryset = CabBooking.objects.all().order_by('-id')
    serializer_class = BookingSerializer
    authentication_classes = (UnsafeSessionAuthentication,)
