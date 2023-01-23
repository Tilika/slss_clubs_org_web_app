from django.db import models

# Create your models here.
class President(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField(default=0)

    def __str__(self):
        return (f"{self.name}, grade {self.grade}")

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.IntegerField(default=0)
    def __str__(self):
        return (f"{self.name}, grade {self.room_number}")

class Club(models.Model):
    description = models.CharField(max_length=200)
    club_name = models.CharField(max_length=100)
    president = models.ForeignKey(President, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    contact = models.EmailField()
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    def __str__(self):
        return (f"{self.club_name}, president is {self.president.name} in grade {self.president.grade}, sponsor is {self.sponsor.name}")

class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    agenda = models.CharField(max_length=50)
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=50)
    open_to = models.CharField(max_length=50)
    sign_up = models.TextField()

    def __str__(self):
        return(f"{self.club.club_name} is hosting a {self.event_type} on {self.date_and_time}")

