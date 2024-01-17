from django.db import models
from devtool.models import DevTool


# Create your models here.
class Idea(models.Model):
    title = models.CharField('아이디어명',max_length=100)
    image = models.ImageField( blank=True, upload_to='ideas/%Y%m%d') # media/ideas/20210901/파일명
    content = models.TextField('아이디어 설명')
    #아이디어 관심도
    interest = models.IntegerField('아이디어 관심도',default=0)
    #개발툴
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE,verbose_name='예상 개발 툴')

    created_date = models.DateTimeField('작성일',auto_created = True, auto_now_add=True)
    updated_date = models.DateTimeField('수정일',auto_created = True, auto_now=True)
    
    def __str__(self):
        return self.title

# class IdeaStar(models.Model):
#     idea = models.ForeignKey(Idea, related_name='starred', on_delete=models.CASCADE)
#     # user = models.ForeignKey(User, related_name='starred_ideas', on_delete=models.CASCADE)
#     created_date = models.DateTimeField('작성일',auto_created = True, auto_now_add=True)

#     class Meta:
#         unique_together = ('idea', 'user',)  # Each user can only star an idea once.

#     def __str__(self):
#         return f"{self.user.username} starred {self.idea.title}"
    
class IdeaStar(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_created=True,auto_now_add=True)

    # class Meta:
    #     unique_together = ('user', 'idea')  # Prevents duplicate entries
