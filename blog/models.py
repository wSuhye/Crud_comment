from django.db import models

# Create your models here.
class Post(models.Model):
    RATING = (
        ('1', '1점'),
        ('2', '2점'),
        ('3', '3점'),
        ('4', '4점'),
        ('5', '5점'),
    )
    title = models.CharField(max_length=200, default="")
    review = models.TextField(default="")
    price = models.CharField(max_length=50, default= "")
    score = models.CharField(max_length = 1, choices = RATING, default= "")    
    
    def __str__(self):
        return self.title

