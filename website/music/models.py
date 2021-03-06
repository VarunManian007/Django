from django.db import models
# from django.core.urlresolvers import reverse

class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title+'-'+self.artist

    # def get_absolute_url(self):
    #     return django.core.urlresolvers.reverse('music:detail',kwargs={'pk':self.pk})

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)#for linking song to album
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


class Login(models.Model):
    email=models.CharField(max_length=100)
    pss=models.CharField(max_length=100)
    is_submit=models.BooleanField(default=False)

