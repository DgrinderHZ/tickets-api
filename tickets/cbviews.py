from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Guest
from .serializers import GuestSerializer


class GuestList(APIView):
    """
    Class based view:
    - List all code guests,
    - or create a new guest.
    """
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GuestPkQuery(APIView):
    """
    Class based view:
    - Retrieve,
    - Update or
    - Delete a guest.
    """
    def get_object(self, pk):
        return get_object_or_404(Guest, pk=pk)

    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
