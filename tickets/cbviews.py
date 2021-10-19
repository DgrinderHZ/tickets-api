from django.shortcuts import get_object_or_404
from rest_framework import status, generics, mixins as mxn
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Guest
from .serializers import GuestSerializer


# Continuation of views.py
# Method 4: REST Class Based View (CBV)
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


# Method 4: REST Class Based View (CBV) using MIXINS
class GuestListMXN(mxn.ListModelMixin,
                   mxn.CreateModelMixin,
                   generics.GenericAPIView):
    """
    Class based view, Mixins Based:
    - List all code guests,
    - or create a new guest.
    """
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class GuestPkQueryMXN(mxn.RetrieveModelMixin,
                      mxn.UpdateModelMixin,
                      mxn.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def delete(self, request, pk):
        return self.destroy(request)
