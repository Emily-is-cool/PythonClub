from django.contrib import admin

from club.views import meetingview, resourceview
from .models import meeting, resource, meetingminute, event

# Register your models here.
admin.site.register(meeting)
admin.site.register(resource)
admin.site.register(meetingminute)
admin.site.register(event)