from rest_framework import serializers as serial
from .models import Guest, Movie, Reservation


class GuestSerializer(serial.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'name', 'mobile', 'reservations']


class MovieSerializer(serial.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReservationSerializer(serial.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
