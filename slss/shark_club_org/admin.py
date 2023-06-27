from django.contrib import admin

from .models import Event, Club


class EventAdmin(admin.ModelAdmin):
    fields = ["club", "location", "agenda"]


class ClubAdmin(admin.ModelAdmin):
    clubs = ["club_name", "president", "sponsor", "description"]


admin.site.register(Event, EventAdmin)
admin.site.register(Club, ClubAdmin)
