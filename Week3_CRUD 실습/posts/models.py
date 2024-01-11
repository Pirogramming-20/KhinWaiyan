from django.db import models

class Post(models.Model): # Post is a table name in DB
    title = models.CharField(max_length=32) # title is an attribute in Post table
    user = models.CharField(max_length=32)
    content = models.TextField()

    def __str__(self):
        return self.title
    

# id, title, user, content
