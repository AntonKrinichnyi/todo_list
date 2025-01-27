from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, related_name='tasks')
    
    
    class Meta:
        ordering = ["-datetime"]