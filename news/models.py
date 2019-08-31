from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class News(models.Model):
    CATEGORY=(("0","Politics"),("1","Fashion"),("2","Business"),("3","Sports"))
    title=models.CharField(max_length=250)
    story= models.TextField()
    count= models.IntegerField(default=0)
    category= models.CharField(choices=CATEGORY, max_length=2)
    slug=models.SlugField(max_length=270)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    cover_image=models.ImageField(upload_to="uploads")
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    
    def get_absolute_url(self):
        return reverse("detail_news",kwargs={"category":self.get_category_display(), "pk":self.pk, "slug":self.slug})

class Comment(models.Model):
    news= models.ForeignKey(News,on_delete=models.CASCADE,related_name="news_comment") 
    comment_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    feedback = models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Title(models.Model):
    title1 = models.CharField(max_length=250)
    class Meta:
        ordering=('title1',)
    def __str__(self):
        return self.title1

class Tag(models.Model):
    tag = models.CharField(max_length=250)
    title2 = models.ManyToManyField(Title)
    class Meta:
        ordering=("tag",)


    def __str__(self):
        return self.tag            