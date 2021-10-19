from rest_framework import serializers as serial
from .models import Guest, Movie, Reservation


class GuestSeriaizer(serial.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'name', 'mobile', 'reservations']


class MovieSeriaizer(serial.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReservationSeriaizer(serial.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
