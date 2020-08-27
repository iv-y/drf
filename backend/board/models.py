from django.db import models
from django.conf import settings

# Create your models here.

class AbstractAuthoredThing:
    """
        Interface for authored things.
        Provide property 'author_str', which appropriately returns the author as a str.
        Require fields 'anonymous', 'author' in self.
    """
    @property
    def author_str(self) -> str:
        if self.anonymous:
            return "(Anon)"
        elif self.author:
            return str(self.author)
        else:
            return "(Unknown)"

class Post(models.Model, AbstractAuthoredThing):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='written_posts')
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked_posts')
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return f'#{self.id} "{self.title}" by {self.author_str}'

class Reply(models.Model, AbstractAuthoredThing):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
    reply_order = models.PositiveIntegerField()
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='written_replies')
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked_replies')
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.post} > reply #{self.reply_order} by {self.author_str}'

