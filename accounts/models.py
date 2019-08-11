from django.db import models

# Create your models here.
class News(models.Model):
    CATEGORY=(("0","Politics"),("1","Sports"),("2","Fashion"),("3","Technology"))
    title = models.CharField(max_length=250)
    story = models.TextField()
    category= models.CharField(max_length=2)
    slug=models.CharField(max_length=270)
    created_at=modesl.models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    