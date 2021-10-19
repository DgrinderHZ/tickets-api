from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

from tickets.models import Guest
from tickets.serializers import GuestSeriaizer


# Method 1: No REST, No Model
def classic(request):
    guests = [
        {
            "id": 1,
            "name": "zeek",
            "mobile": "0656139568",
        },
        {
            "id": 2,
            "name": "zone",
            "mobile": "0656139568",
        }
    ]
    return JsonResponse(guests, safe=False)


# Method 2: No REST, With Model
def withModel(request):
    guests = Guest.objects.all()
    data = {"guests": list(guests.values())}
    return JsonResponse(data)


# Method 3: REST Function Based View (FBV)
@api_view(['GET', 'POST'])
def guest_list(request):
    """
    Function based view:
    - List all code guests, 
    - or create a new guest.
    """
    if request.method == "GET":
        guests = Guest.objects.all()
        serializer = GuestSeriaizer(guests, many=True)
        return Response(serializer.data)
    else:
        serializer = GuestSeriaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def guest_pk_query(request, pk):
    """
    Function based view:
    - Retrieve,
    - Update or
    - Delete a guest.
    """
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == "GET":
        serializer = GuestSeriaizer(guest)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = GuestSeriaizer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def api_root(request, format=None):
    """
    Function based view:
    -  Snippets API root.
    """
    return Response({
        'jsonresno_guests': reverse('jsonresno_guests', request=request, format=format),
        'jsonresmo_guests': reverse('jsonresmo_guests', request=request, format=format),
        'fbv_guest_list': reverse('fbv_guest_list', request=request, format=format),

    })
