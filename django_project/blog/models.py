from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # si borra el post no se borra el user
    
    def __str__(self):
        return 'Title: %s, Author: %s' % (self.title, self.author)

    # para redirigir (reverse) a 'post-detail'
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})