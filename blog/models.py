from django.db import models
from users.models import MyUser
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    count_view = models.PositiveIntegerField(default=0)
    count_like = models.PositiveIntegerField(default=0)
    count_comment = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title


class PostComment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='post_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    content = models.TextField()
    count_like = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name or f"Comment by {self.user.username} on Post {self.post.id}"
    
    
class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='post_like')
    
    class Meta:
        unique_together = ('post', 'user')
    
    def __str__(self):
        return f'{self.user} likes {self.post}'
    
    
class PostCommentLike(models.Model):
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE, related_name='post_comment_like')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='post_comment_like')
    
    class Meta:
        unique_together = ('comment', 'user')
    
    def __str__(self):
        return f'{self.user} likes {self.comment}'
    