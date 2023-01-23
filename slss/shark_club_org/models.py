from django.db import models

# Create your models here.
class President(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)

class Club(models.Model):
    description = models.CharField(max_length=200)
    club_name = models.CharField(max_length=100)
    president = models.ForeignKey(President, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    contact = models.EmailField()
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    agenda = models.CharField(max_length=50)
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=50)
    open_to = models.CharField(max_length=50)
    sign_up = models.TextField()


