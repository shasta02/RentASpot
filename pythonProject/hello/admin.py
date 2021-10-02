from django.contrib import admin
from datetime import timedelta, datetime

from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils.http import urlencode

from .models import RenterModel

@admin.register(RenterModel)
class RenterModel(admin.ModelAdmin):
    list_display1 = ("spots_available")
    list_display2 = ("renter_price")
    list_display3 = ("renter_location")
    list_display4 = ("renter_date")
    list_display5 = ("TIMING_CHOICES")





