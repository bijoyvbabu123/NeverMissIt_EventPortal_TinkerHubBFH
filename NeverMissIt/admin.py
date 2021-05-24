from django.contrib import admin
from NeverMissIt.models import EventDetails, EventParticipants

# Register your models here.

# registered these models to facilitate the admin user to access these from the admin dashboard.
admin.site.register(EventDetails)
admin.site.register(EventParticipants)