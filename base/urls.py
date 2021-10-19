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
from tickets import views, cbviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jsonresno/', views.classic, name='jsonresno_guests'),
    path('jsonresmodel/', views.withModel, name='jsonresmo_guests'),
    path('rest/fbv/guests/', views.guest_list, name='fbv_guest_list'),
    path('rest/fbv/guests/<int:pk>/', views.guest_pk_query, name='fbv_guest_pk_query'),
    path('rest/cbv/guests/', cbviews.GuestList.as_view(), name='cbv_guest_list'),
    path('rest/cbv/guests/<int:pk>/', cbviews.GuestPkQuery.as_view(), name='cbv_guest_pk_query'),

    path('', views.api_root),
]
