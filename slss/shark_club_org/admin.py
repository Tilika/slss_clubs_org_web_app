from django.contrib import admin

from .models import Event, Club, President, Sponsor


class EventAdmin(admin.ModelAdmin):
    fields = ["club", "location", "agenda", "date_and_time"]


class ClubAdmin(admin.ModelAdmin):
    clubs = ["club_name", "president", "sponsor", "description"]


class PresidentAdmin(admin.ModelAdmin):
    president = ["name", "grade"]


class SponsorAdmin(admin.ModelAdmin):
    sponsor = ["name", "room_number"]


admin.site.register(Event, EventAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(President, PresidentAdmin)
admin.site.register(Sponsor, SponsorAdmin)
