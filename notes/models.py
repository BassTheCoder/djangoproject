from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
      return self.title

    def get_absolute_url(self):
        return reverse('note-view', kwargs={'pk': self.pk})
