from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="views"),
    # 127.0.0.1:8000/shark_club_org/
    path("events/<int:club_id>", views.event_view, name="events"),
]
