from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# TODO: Events view when student is logged in
#       All events
#       Filters
def event_view(request):
    # Get all future events
    # Create the html
    # return the http response

    return None



