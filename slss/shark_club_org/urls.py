from django.urls import path, include
from . import views

urlpatterns = [
    path(r'^$', views.index, name="index") 
    # 127.0.0.1:8000/shark_club_org/
]