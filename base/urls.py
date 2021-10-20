"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from tickets import views, cbviews


router = DefaultRouter()
router.register("guests", cbviews.GuestViewSet, basename='guests')
router.register("movies", cbviews.MovieViewSet, basename='movies')
router.register("reservations", cbviews.ReservationViewSet, basename='reservations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jsonresno/', views.classic, name='jsonresno_guests'),
    path('jsonresmodel/', views.withModel, name='jsonresmo_guests'),
    path('rest/fbv/guests/', views.guest_list, name='fbv_guest_list'),

    # find movie 
    path('rest/fbv/findmovie', views.find_movie, name='fbv_find_movie'),

    #9 new reservation
    path('rest/fbv/newreservation',views.new_reservation, name='fbv_newreservation'),

    path('rest/fbv/guests/<int:pk>/', views.guest_pk_query, name='fbv_guest_pk_query'),
    path('rest/cbv/guests/', cbviews.GuestList.as_view(), name='cbv_guest_list'),
    path('rest/cbv/guests/<int:pk>/', cbviews.GuestPkQuery.as_view(), name='cbv_guest_pk_query'),
    path('rest/mxn/guests/', cbviews.GuestListMXN.as_view(), name='mxn_guest_list'),
    path('rest/mxn/guests/<int:pk>/', cbviews.GuestPkQueryMXN.as_view(), name='mxn_guest_pk_query'),
    path('rest/gnrx/guests/', cbviews.GuestListGNRX.as_view(), name='gnrx_guest_list'),
    path('rest/gnrx/guests/<int:pk>/', cbviews.GuestPkQueryGNRX.as_view(), name='gnrx_guest_pk_query'),
    path('rest/viewsets/', include(router.urls)),
    path('', views.api_root),
]
