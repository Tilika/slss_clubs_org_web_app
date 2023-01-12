from django.urls import path, include
from . import views

urlpatterns = [
   path('index/', views.index, name='main-view') 
    # 127.0.0.1:8000/shark_club_org/
]