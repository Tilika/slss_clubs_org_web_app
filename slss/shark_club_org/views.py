from django.shortcuts import render, get_object_or_404

from .models import Event

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the events index.")


# TODO: Events view when student is logged in
#       All events
#       Filters


def event_view(request, event_id):
    # Get all future events
    # Create the html
    # return the http response

    event = get_object_or_404(Event, pk=event_id)

    return render(request, "shark_club_org/events.html", {"event": event})
