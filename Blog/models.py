from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="article",null=True,blank=True)
    titel=models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="blog/image")
    created=models.DateTimeField(auto_now_add=True)
    discription=models.TextField()

    def __str__(self):

        return self.titel

class Comment(models.Model):
    article=models.ForeignKey(Article,related_name="comment",on_delete=models.CASCADE)
    text=models.TextField()

    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.text[:30]



