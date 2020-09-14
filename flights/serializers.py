from rest_framework import serializers

from .models import Flight, Booking


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['id','destination', 'time', 'price']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['id', 'flight', 'date',]


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['id', 'flight', 'date', 'passengers']


class BookingUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['passengers', 'date']
