from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    amount = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text


class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=280)
    created_date = models.DateTimeField(default=timezone.now)
    delete_flg = models.BooleanField(default=False)

    def comment_delete(self):
        self.delete_flg = True
        self.save()

    def __str__(self):
        return self.comment
