from django.shortcuts import get_object_or_404
from rest_framework import status, generics, mixins as mxn
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Guest, Movie, Reservation
from .serializers import GuestSerializer,\
    MovieSerializer, ReservationSerializer


# Continuation of views.py
# Method 4: REST Class Based View (CBV)
class GuestList(APIView):
    """
    Class based view:
    - List all code guests,
    - or create a new guest.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
    """
    Class based view, Mixins Based:
    - Retrieve,
    - Update or
    - Delete a guest.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def delete(self, request, pk):
        return self.destroy(request)


# Method 5: REST Class Based View (CBV) using generics
class GuestListGNRX(generics.ListCreateAPIView):
    """
    Class based view, generics Based:
    - List all code guests,
    - or create a new guest.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class GuestPkQueryGNRX(generics.RetrieveUpdateDestroyAPIView):
    """
    Class based view, generics Based:
    - Retrieve,
    - Update or
    - Delete a guest.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


# Method 6: REST Class Based View (CBV) using viewsets
# All In One CRUD
class GuestViewSet(viewsets.ModelViewSet):
    """
    Class based view, viewset Based:
    - List all code guests,
    - Create,
    - Retrieve,
    - Update or
    - Delete a guest.
    """
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class MovieViewSet(viewsets.ModelViewSet):
    """
    Class based view, viewset Based:
    - List all code Movies,
    - Create,
    - Retrieve,
    - Update or
    - Delete a Movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ReservationViewSet(viewsets.ModelViewSet):
    """
    Class based view, viewset Based:
    - List all code Reservations,
    - Create,
    - Retrieve,
    - Update or
    - Delete a Reservation.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
