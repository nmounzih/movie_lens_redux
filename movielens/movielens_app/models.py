from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length = 100)
    release_date = models.CharField(max_length = 75)
    imdb_link = models.CharField(max_length= 100)


class Rater(models.Model):
    age = models.CharField(max_length = 3)
    gender = models.CharField(max_length = 1)
    job = models.CharField(max_length = 20)
    zipcode = models.CharField(max_length = 15)


class Rating(models.Model):
    rater = models.ForeignKey(Rater, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    rating = models.IntegerField()
    timestamp = models.CharField(max_length = 35)
