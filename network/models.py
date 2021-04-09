from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass

class Posts(models.Model):
    posts = models.CharField(max_length=50)
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())
    like = models.ManyToManyField('User',blank='True',related_name='Likes')

    class Meta:
        ordering =['-date']

class Profile(models.Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    followers = models.ManyToManyField('User',related_name='Followers',blank='True')
    following = models.ManyToManyField('User',related_name='Following',blank='True')

    def __str__(self):
        return str(self.user)
