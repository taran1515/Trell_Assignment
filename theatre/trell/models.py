from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=100)
    duration = models.TimeField()

    def __str__(self):
        return self.name

class MovieTimings(models.Model):
    movie_name = models.ForeignKey(Movie,on_delete=models.CASCADE)
    timings = models.DateTimeField()
    price = models.IntegerField()
    ticket = models.IntegerField()
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return str(self.movie_name)+' ' + str(self.timings)

    def purchase_ticket(self):
        self.purchased = True




