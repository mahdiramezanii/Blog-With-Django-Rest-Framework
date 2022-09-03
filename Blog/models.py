from django.db import models

class Article(models.Model):

    titel=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    discription=models.TextField()



    def __str__(self):

        return self.titel

