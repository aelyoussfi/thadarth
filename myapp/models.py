from django.db import models
from authentication.models import User
# Create your models here.

class Comment(models.Model):
    content = models.TextField(max_length = 31)
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User,on_delete =models.CASCADE) 
    
class Post(models.Model):
    content = models.TextField(max_length = 1007)
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User,on_delete =models.CASCADE) 
    comment = models.ManyToManyField(Comment)

    def count_likes(self):
        return Like.objects.filter(post=self).count()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'post']  # Ensures a user can like a post only once

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'post']  # Ensures a user can dislike a post only once

"""
    In this implementation:

Likes and Dislikes as Separate Models: Each like and dislike is represented as a separate model. 
This allows for easy expansion and modification in the future.

ForeignKey Relationships: The Like and Dislike models have a ForeignKey to both User and Post.
 This establishes a relationship between the user, the post, and the like/dislike.

Unique Together Constraint: The unique_together Meta option in Like and Dislike models ensures that
 a user can only like or dislike a specific post once. It prevents duplicate likes/dislikes from the 
 same user on the same post.

Many-to-Many Field in Post for Comments: The Post model has a ManyToManyField for comments,
 allowing multiple comments to be associated with a single post. The blank=True attribute allows 
 a post to have no comments.

Remember to run python manage.py makemigrations and python manage.py migrate after changing
 your models to apply these changes to your database schema.
"""