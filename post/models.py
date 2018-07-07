from django.db import models
from django.urls import reverse
from core.models import UserProfile
# Create your models here.


class Post(models.Model):
    userprofile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=True, null=True)
    containt = models.CharField(max_length=99999999, blank=True, null=True)
    image = models.ImageField(
        upload_to='Post/%Y/%m/%d/', blank=True, null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Post:home')


class PostComment(models.Model):
    post_comment = models.CharField(max_length=999999, blank=True, null=True)
    post = models.ManyToManyField(Post)
    userprofile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="profile")
    # creade = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Post_comment


class like(models.Model):
    post_like = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    userprofile = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, related_name="post_like")
    # creade = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
