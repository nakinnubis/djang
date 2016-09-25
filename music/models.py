from django.db import models

# Create your models here.

#creating models for my music app
#create a class first

class Albums(models.Model):
        artist = models.CharField(max_length = 250)
        artist_album = models.CharField(max_length = 500)
        genre = models.CharField(max_length = 100)
        album_logo = models.CharField(max_length = 1000)
        def __str__(self):
            return self.artist +' '+ self.artist_album + self.genre

class Song(models.Model):
    album = models.ForeignKey(Albums, on_delete = models.CASCADE)
    file_type = models.CharField(max_length= 100)
    song_title = models.CharField(max_length =100)
