from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image_url = models.URLField(default='https://picsum.photos/200/300')  # Default image URL
    
    director = models.CharField(max_length=100)
    actors = models.TextField()  # multiple actors as a comma-separated list
    running_time = models.IntegerField()  # In minutes
    content = models.TextField()  # The review text
