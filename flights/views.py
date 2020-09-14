from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, DestroyAPIView
from datetime import datetime

from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer, BookingUpdateSerializer, BookingDetailsSerializer


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer

class BookingsDetails(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDetailsSerializer
	lookup_field  = 'id'
	lookup_url_kwarg = 'booking_id'

class BookingsUpdate(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'

class BookingsDelete(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


