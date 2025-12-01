from django.contrib import admin
from .models import CandidateUser, Event
from django.contrib.auth.admin import UserAdmin

admin.site.register(CandidateUser, UserAdmin)
admin.site.register(Event)
