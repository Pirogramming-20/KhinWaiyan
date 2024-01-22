from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField( blank=True, upload_to='main/%Y%m%d') # media/main/20210901/파일명
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') #post.comments.all() instead of post.comment_set.all(
    content = models.TextField(default='')  
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author} on {self.post}'
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes') #post.likes.all() instead of post.like_set.all()
    
    class Meta:
        unique_together = ['user', 'post'] # Each user can like a post only once
    def __str__(self):
        return f'{self.user} on {self.post}'

