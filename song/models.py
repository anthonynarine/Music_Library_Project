from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length= 100)                                                     
    artist = models.CharField(max_length= 100)                                                     
    album = models.CharField(max_length= 100)                                                     
    genre = models.CharField(max_length= 100)
    # this shold all users to enter a date. https://www.youtube.com/watch?v=Lyq7Bn4c6Kc                                                     
    release_date = models.DateField("mm/dd/year",auto_now_add=False, auto_now=False, blank=True, null=True)