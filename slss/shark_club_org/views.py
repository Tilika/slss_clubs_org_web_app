from django.shortcuts import render, get_object_or_404

from .models import Club
from .models import Event

# Create your views here.
from django.http import HttpResponse


def index(request):
    clubs = Club.objects.all()
    context = {'clubs': clubs}
    return render(request, "shark_club_org/home.html", context)
    #return HttpResponse("Hello, world. You're at the events index.")


# TODO: Events view when student is logged in
#       All events
#       Filters


def event_view(request, club_id):
    # Get all future events
    # Create the html
    # return the http response

    #event = get_object_or_404(Event, pk=event_id)
    events = Event.objects.all()
    eventsc = []
    for event in events: 
        if (event.club.id == club_id):
            eventsc.append(event)

    context = {'eventsc': eventsc}
    return render(request, "shark_club_org/events.html", context)
