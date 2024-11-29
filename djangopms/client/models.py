from django.contrib.auth.models import User
from django.db import models
from team.models import Team
# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)


class Client(models.Model):
    team = models.ForeignKey(Team, related_name ='clients', on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    
    comments = models.ManyToManyField(Comment, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering=['-name',]
        verbose_name = 'Hello'
        verbose_name_plural='Helloos'



    def __str__(self):
        return f'Client: {self.name}'
    
    def number_of_comments(self):
        return self.comments.count()

class Todolist(models.Model):
    client = models.ForeignKey(Client, related_name='todolists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comments = models.ManyToManyField(Comment, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, related_name='todolists', on_delete=models.CASCADE)
