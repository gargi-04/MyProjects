from django.contrib import admin
from .models import Venue,Ticket
# Register your models here.
admin.site.register((Venue,Ticket))