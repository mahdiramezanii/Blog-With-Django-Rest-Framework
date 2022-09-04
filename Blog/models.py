from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="article",null=True,blank=True)
    titel=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    discription=models.TextField()



    def __str__(self):

        return self.titel

